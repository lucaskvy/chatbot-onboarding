// ============================================================
//  Lagos Analytics Chatbot — Frontend JS
//  POST /chat  →  { pergunta: string }  →  { resposta: string }
// ============================================================

const API_URL = '/chat';

// DOM refs
const messagesEl    = document.getElementById('messages');
const inputEl       = document.getElementById('user-input');
const sendBtn       = document.getElementById('send-btn');
const welcomeScreen = document.getElementById('welcome-screen');
const badgeDot      = document.getElementById('badge-dot');
const statusText    = document.getElementById('status-text');
const logoImg       = document.getElementById('logo-img');
const logoFallback  = document.getElementById('logo-fallback');
const canvas        = document.getElementById('particles-canvas');

let isLoading = false;

// ────────────────────────────────────────────────────────────
// Logo fallback — show SVG if image fails to load
// ────────────────────────────────────────────────────────────
if (logoImg) {
  logoImg.addEventListener('error', () => {
    logoImg.style.display = 'none';
    if (logoFallback) logoFallback.style.display = 'flex';
  });
}

// ────────────────────────────────────────────────────────────
// Status check — ping the API on startup
// ────────────────────────────────────────────────────────────
async function checkStatus() {
  try {
    const res = await fetch('/', { method: 'GET', signal: AbortSignal.timeout(5000) });
    if (res.ok) {
      badgeDot.classList.add('online');
      statusText.textContent = 'Online';
    } else {
      throw new Error('API error');
    }
  } catch {
    badgeDot.classList.add('error');
    statusText.textContent = 'Offline';
  }
}

// ────────────────────────────────────────────────────────────
// Auto-resize textarea
// ────────────────────────────────────────────────────────────
inputEl.addEventListener('input', () => {
  inputEl.style.height = 'auto';
  inputEl.style.height = Math.min(inputEl.scrollHeight, 140) + 'px';
});

// Enter to send, Shift+Enter for new line
inputEl.addEventListener('keydown', (e) => {
  if (e.key === 'Enter' && !e.shiftKey) {
    e.preventDefault();
    sendMessage();
  }
});

// ────────────────────────────────────────────────────────────
// Quick question buttons
// ────────────────────────────────────────────────────────────
function useQuickQuestion(btn) {
  const text = btn.innerText.replace(/^[^\s]+\s/, ''); // remove emoji
  inputEl.value = text;
  inputEl.style.height = 'auto';
  inputEl.style.height = Math.min(inputEl.scrollHeight, 140) + 'px';
  inputEl.focus();
  sendMessage();
}

// ────────────────────────────────────────────────────────────
// Send message
// ────────────────────────────────────────────────────────────
async function sendMessage() {
  const text = inputEl.value.trim();
  if (!text || isLoading) return;

  // Hide welcome screen on first message
  if (welcomeScreen && welcomeScreen.style.display !== 'none') {
    welcomeScreen.style.display = 'none';
  }

  // Clear input
  inputEl.value = '';
  inputEl.style.height = 'auto';

  // Append user message
  appendMessage('user', text);

  // Show typing indicator
  const typingEl = appendTypingIndicator();

  setLoading(true);

  try {
    const res = await fetch(API_URL, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ pergunta: text }),
    });

    const data = await res.json();

    typingEl.remove();

    if (!res.ok) {
      const errMsg = data?.detail || `Erro ${res.status}: não foi possível obter resposta.`;
      appendMessage('bot', errMsg, true);
    } else {
      appendMessage('bot', data.resposta);
    }
  } catch (err) {
    typingEl.remove();
    appendMessage('bot', '⚠️ Não foi possível conectar ao servidor. Verifique sua conexão ou tente novamente.', true);
  } finally {
    setLoading(false);
    scrollToBottom();
  }
}

// ────────────────────────────────────────────────────────────
// Append a message bubble
// ────────────────────────────────────────────────────────────
function appendMessage(role, text, isError = false) {
  const row = document.createElement('div');
  row.classList.add('message', role);

  // Avatar
  const avatar = document.createElement('div');
  avatar.classList.add('avatar', role === 'bot' ? 'avatar-bot' : 'avatar-user');
  avatar.innerHTML = role === 'bot'
    ? `<svg viewBox="0 0 24 24" fill="none">
         <circle cx="12" cy="12" r="10" stroke="#00e5ff" stroke-width="1.5"/>
         <circle cx="12" cy="12" r="4" fill="#00e5ff"/>
       </svg>`
    : 'EU';

  // Bubble
  const bubble = document.createElement('div');
  bubble.classList.add('bubble');
  if (isError) bubble.classList.add('error-bubble');

  // Render simple markdown: bold, italic, inline code, line breaks
  bubble.innerHTML = renderMarkdown(text);

  row.appendChild(avatar);
  row.appendChild(bubble);
  messagesEl.appendChild(row);
  scrollToBottom();
  return row;
}

// ────────────────────────────────────────────────────────────
// Typing indicator
// ────────────────────────────────────────────────────────────
function appendTypingIndicator() {
  const row = document.createElement('div');
  row.classList.add('message', 'bot');

  const avatar = document.createElement('div');
  avatar.classList.add('avatar', 'avatar-bot');
  avatar.innerHTML = `<svg viewBox="0 0 24 24" fill="none">
    <circle cx="12" cy="12" r="10" stroke="#00e5ff" stroke-width="1.5"/>
    <circle cx="12" cy="12" r="4" fill="#00e5ff"/>
  </svg>`;

  const bubble = document.createElement('div');
  bubble.classList.add('bubble');
  bubble.innerHTML = `<div class="typing-indicator">
    <span></span><span></span><span></span>
  </div>`;

  row.appendChild(avatar);
  row.appendChild(bubble);
  messagesEl.appendChild(row);
  scrollToBottom();
  return row;
}

// ────────────────────────────────────────────────────────────
// Simple markdown renderer
// ────────────────────────────────────────────────────────────
function renderMarkdown(text) {
  return text
    // Escape HTML entities first
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    // Code blocks ```...```
    .replace(/```[\s\S]*?```/g, (m) => {
      const code = m.slice(3, -3).replace(/^\w*\n/, '');
      return `<pre style="background:rgba(0,0,0,0.3);border:1px solid rgba(255,255,255,0.1);border-radius:8px;padding:12px;overflow-x:auto;font-size:13px;margin:8px 0;"><code>${code}</code></pre>`;
    })
    // Inline code `...`
    .replace(/`([^`]+)`/g, '<code style="background:rgba(0,229,255,0.12);color:#00e5ff;padding:2px 6px;border-radius:4px;font-size:13px;">$1</code>')
    // Bold **text**
    .replace(/\*\*(.+?)\*\*/g, '<strong>$1</strong>')
    // Italic *text*
    .replace(/\*(.+?)\*/g, '<em>$1</em>')
    // Links [text](url)
    .replace(/\[([^\]]+)\]\((https?:\/\/[^\)]+)\)/g, '<a href="$2" target="_blank" rel="noopener">$1</a>')
    // Unordered lists (- item or • item)
    .replace(/^[-•]\s+(.+)$/gm, '<li>$1</li>')
    .replace(/(<li>.*<\/li>)/s, '<ul style="padding-left:20px;margin:8px 0;">$1</ul>')
    // Line breaks
    .replace(/\n/g, '<br/>');
}

// ────────────────────────────────────────────────────────────
// Loading state
// ────────────────────────────────────────────────────────────
function setLoading(state) {
  isLoading = state;
  sendBtn.disabled = state;
  inputEl.disabled = state;
}

// ────────────────────────────────────────────────────────────
// Scroll to bottom
// ────────────────────────────────────────────────────────────
function scrollToBottom() {
  const container = document.getElementById('chat-container');
  requestAnimationFrame(() => {
    container.scrollTop = container.scrollHeight;
  });
}

// ────────────────────────────────────────────────────────────
// Particle system — recreating the Lagos website aesthetic
// ────────────────────────────────────────────────────────────
(function initParticles() {
  const ctx = canvas.getContext('2d');
  let W, H, particles = [];

  const PARTICLE_COUNT = 80;
  const COLORS = ['#00e5ff', '#ff1177', '#a855f7', '#ffffff'];

  function resize() {
    W = canvas.width  = window.innerWidth;
    H = canvas.height = window.innerHeight;
  }

  function createParticle() {
    return {
      x: Math.random() * W,
      y: Math.random() * H,
      r: Math.random() * 1.8 + 0.4,
      color: COLORS[Math.floor(Math.random() * COLORS.length)],
      alpha: Math.random() * 0.5 + 0.1,
      vx: (Math.random() - 0.5) * 0.25,
      vy: (Math.random() - 0.5) * 0.25,
      twinkle: Math.random() * Math.PI * 2,
      twinkleSpeed: Math.random() * 0.02 + 0.005,
    };
  }

  function init() {
    resize();
    particles = Array.from({ length: PARTICLE_COUNT }, createParticle);
  }

  function draw() {
    ctx.clearRect(0, 0, W, H);

    for (const p of particles) {
      p.x += p.vx;
      p.y += p.vy;
      p.twinkle += p.twinkleSpeed;

      // Wrap around edges
      if (p.x < -5) p.x = W + 5;
      if (p.x > W + 5) p.x = -5;
      if (p.y < -5) p.y = H + 5;
      if (p.y > H + 5) p.y = -5;

      const alpha = p.alpha * (0.6 + 0.4 * Math.sin(p.twinkle));

      ctx.beginPath();
      ctx.arc(p.x, p.y, p.r, 0, Math.PI * 2);
      ctx.fillStyle = p.color;
      ctx.globalAlpha = alpha;
      ctx.fill();
    }

    ctx.globalAlpha = 1;
    requestAnimationFrame(draw);
  }

  window.addEventListener('resize', () => {
    resize();
  });

  init();
  draw();
})();

// ────────────────────────────────────────────────────────────
// Init
// ────────────────────────────────────────────────────────────
checkStatus();
inputEl.focus();
