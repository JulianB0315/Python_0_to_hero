// Variables globales
const chatMessages = document.getElementById('chat-messages');
const mensajeInput = document.getElementById('mensaje-input');
const enviarBtn = document.getElementById('enviar-btn');
const productosContainer = document.getElementById('productos-sugeridos');
const modal = document.getElementById('product-modal');
const productDetails = document.getElementById('product-details');
const carritoMini = document.getElementById('carrito-mini');
const carritoTotal = document.getElementById('carrito-total');

let carrito = [];

// Evento de envío
enviarBtn.addEventListener('click', () => {
    const mensaje = mensajeInput.value.trim();
    if (mensaje) {
        enviarMensaje(mensaje);
    }
});

// Enter para enviar
mensajeInput.addEventListener('keypress', (e) => {
    if (e.key === 'Enter' && !e.shiftKey) {
        e.preventDefault();
        enviarBtn.click();
    }
});

// Función para enviar mensaje
async function enviarMensaje(mensaje) {
    // Agregar mensaje del usuario
    agregarMensaje(mensaje, 'user');
    
    // Limpiar input
    mensajeInput.value = '';
    mensajeInput.focus();
    
    // Mostrar indicador de escritura
    mostrarIndicadorEscritura();
    
    try {
        // Enviar al servidor
        const response = await fetch('/api/chat', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ mensaje })
        });
        
        const data = await response.json();
        
        // Remover indicador
        removerIndicadorEscritura();
        
        // Agregar respuesta del bot
        agregarMensaje(data.respuesta, 'bot');
        
        // Actualizar carrito
        if (data.carrito) {
            carrito = data.carrito;
            actualizarCarritoUI();
        }
        
        // Mostrar productos si hay
        if (data.productos && data.productos.length > 0) {
            mostrarProductos(data.productos);
        } else {
            productosContainer.innerHTML = '';
        }
        
        // Auto-scroll
        chatMessages.scrollTop = chatMessages.scrollHeight;
        
    } catch (error) {
        console.error('Error:', error);
        removerIndicadorEscritura();
        agregarMensaje('Lo siento, hubo un error. Intenta de nuevo.', 'bot');
    }
}

// Función para agregar mensaje al chat
function agregarMensaje(texto, tipo) {
    const messageDiv = document.createElement('div');
    messageDiv.className = `message ${tipo}-message`;
    
    const contentDiv = document.createElement('div');
    contentDiv.className = 'message-content';
    
    // Procesar markdown simple
    let htmlText = procesarMarkdown(texto);
    contentDiv.innerHTML = htmlText;
    
    messageDiv.appendChild(contentDiv);
    chatMessages.appendChild(messageDiv);
    
    // Scroll al final
    chatMessages.scrollTop = chatMessages.scrollHeight;
}

// Función para procesar markdown simple
function procesarMarkdown(texto) {
    return texto
        .replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>')
        .replace(/\*(.*?)\*/g, '<em>$1</em>')
        .replace(/_(.*?)_/g, '<u>$1</u>')
        .replace(/\n/g, '<br>');
}

// Indicador de escritura
function mostrarIndicadorEscritura() {
    const typingDiv = document.createElement('div');
    typingDiv.className = 'message bot-message typing-indicator';
    typingDiv.id = 'typing-indicator';
    
    const contentDiv = document.createElement('div');
    contentDiv.className = 'message-content';
    contentDiv.innerHTML = '<span>●</span><span>●</span><span>●</span>';
    
    typingDiv.appendChild(contentDiv);
    chatMessages.appendChild(typingDiv);
    chatMessages.scrollTop = chatMessages.scrollHeight;
}

function removerIndicadorEscritura() {
    const typing = document.getElementById('typing-indicator');
    if (typing) typing.remove();
}

// Función para mostrar productos
function mostrarProductos(productos) {
    productosContainer.innerHTML = '';
    
    productos.forEach(prod => {
        const card = document.createElement('div');
        card.className = 'producto-card';
        card.innerHTML = `
            <h4>${prod.nombre}</h4>
            <p>${prod.descripcion.substring(0, 50)}...</p>
            <div class="producto-precio">$${prod.precio}</div>
            <button class="producto-btn" onclick="agregarAlCarrito(${prod.id}, '${prod.nombre}', ${prod.precio})">
                Agregar al carrito
            </button>
        `;
        card.style.cursor = 'pointer';
        card.addEventListener('click', () => mostrarDetalleProducto(prod));
        
        productosContainer.appendChild(card);
    });
}

// Función para mostrar detalles de producto
function mostrarDetalleProducto(producto) {
    productDetails.innerHTML = `
        <h2>${producto.nombre}</h2>
        <p><strong>Categoría:</strong> ${producto.categoria}</p>
        <p><strong>Precio:</strong> <span style="color: #51cf66; font-size: 18px;">$${producto.precio}</span></p>
        <p>${producto.descripcion}</p>
        <div class="specs">
            <h3>Especificaciones</h3>
            <p>${producto.especificaciones}</p>
        </div>
        <button class="btn-enviar" style="width: 100%;" onclick="agregarAlCarrito(${producto.id}, '${producto.nombre}', ${producto.precio}); cerrarModal();">
            Agregar al carrito
        </button>
    `;
    modal.style.display = 'block';
}

// Función para agregar al carrito
function agregarAlCarrito(id, nombre, precio) {
    enviarMensaje(`Agrégame ${nombre}`);
}

// Cerrar modal
function cerrarModal() {
    modal.style.display = 'none';
}

document.querySelector('.close').addEventListener('click', cerrarModal);

window.addEventListener('click', (event) => {
    if (event.target === modal) {
        cerrarModal();
    }
});

// Función para actualizar UI del carrito
function actualizarCarritoUI() {
    if (carrito.length === 0) {
        carritoMini.innerHTML = '<p class="carrito-vacio">Vacío</p>';
        carritoTotal.innerHTML = '';
        return;
    }
    
    let html = '';
    let total = 0;
    
    carrito.forEach((item, index) => {
        html += `
            <div class="carrito-item">
                ${index + 1}. ${item.nombre} - $${item.precio}
            </div>
        `;
        total += item.precio;
    });
    
    carritoMini.innerHTML = html;
    carritoTotal.innerHTML = `💰 Total: $${total.toFixed(2)}`;
}

// Agregar estilos dinámicos para animación de escritura
const style = document.createElement('style');
style.innerHTML = `
    .typing-indicator .message-content span {
        animation: blink 1.4s infinite;
        margin: 0 2px;
    }
    
    .typing-indicator .message-content span:nth-child(2) {
        animation-delay: 0.2s;
    }
    
    .typing-indicator .message-content span:nth-child(3) {
        animation-delay: 0.4s;
    }
    
    @keyframes blink {
        0%, 60%, 100% {
            opacity: 0.5;
        }
        30% {
            opacity: 1;
        }
    }
`;
document.head.appendChild(style);

// Mensaje de bienvenida simplificado
window.addEventListener('load', () => {
    console.log('🤖 TechStore Bot cargado correctamente');
    mensajeInput.focus();
});

// Función para hacer que enviarMensaje sea global
window.enviarMensaje = enviarMensaje;
window.agregarAlCarrito = agregarAlCarrito;
