// media/webview/agent.js — Runs INSIDE the webview (browser context)

(function () {
  const vscode = acquireVsCodeApi();

  // DOM elements
  const canvas = document.getElementById('avatar-canvas');
  const ctx = canvas ? canvas.getContext('2d') : null;
  const statusText = document.getElementById('status-text');
  const statusIndicator = document.getElementById('status-indicator');
  const chatMessages = document.getElementById('chat-messages');
  const chatForm = document.getElementById('chat-form');
  const chatInput = document.getElementById('chat-input');
  const btnPause = document.getElementById('btn-pause');
  const btnSpeed = document.getElementById('btn-speed');

  // State
  let state = {
    running: true,
    paused: false,
    avatar: 'robot-default',
    speed: 1,
    focusMode: false,
    chatLoading: false
  };

  // --- Animation loop (FPS-capped at 30) ---
  const FPS_CAP = 30;
  const FRAME_DURATION = 1000 / FPS_CAP;
  let lastFrameTime = 0;
  let animationFrame = 0;

  function drawFrame(timestamp) {
    if (!state.running) { return; }
    if (state.paused) {
      requestAnimationFrame(drawFrame);
      return;
    }

    // Respect prefers-reduced-motion
    const reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    if (reduceMotion) {
      drawStaticAvatar();
      return;
    }

    // FPS cap
    const elapsed = timestamp - lastFrameTime;
    if (elapsed < FRAME_DURATION / state.speed) {
      requestAnimationFrame(drawFrame);
      return;
    }
    lastFrameTime = timestamp;
    animationFrame++;

    if (ctx) {
      ctx.clearRect(0, 0, canvas.width, canvas.height);

      const centerX = canvas.width / 2;
      const centerY = canvas.height / 2;
      const bounce = Math.sin(animationFrame * 0.05) * 10;

      // Body
      ctx.beginPath();
      ctx.arc(centerX, centerY + bounce, 40, 0, Math.PI * 2);
      ctx.fillStyle = state.chatLoading ? '#ff9800' : '#4caf50';
      ctx.fill();

      // Eyes
      ctx.fillStyle = '#fff';
      ctx.beginPath();
      ctx.arc(centerX - 12, centerY + bounce - 8, 6, 0, Math.PI * 2);
      ctx.arc(centerX + 12, centerY + bounce - 8, 6, 0, Math.PI * 2);
      ctx.fill();

      // Pupils (animated for "alive" look)
      const pupilOffset = Math.sin(animationFrame * 0.02) * 2;
      ctx.fillStyle = '#333';
      ctx.beginPath();
      ctx.arc(centerX - 12 + pupilOffset, centerY + bounce - 8, 3, 0, Math.PI * 2);
      ctx.arc(centerX + 12 + pupilOffset, centerY + bounce - 8, 3, 0, Math.PI * 2);
      ctx.fill();

      // Mouth (changes with loading state)
      ctx.beginPath();
      if (state.chatLoading) {
        // Open mouth when thinking
        ctx.arc(centerX, centerY + bounce + 10, 8, 0, Math.PI);
        ctx.fillStyle = '#333';
        ctx.fill();
      } else {
        // Smile
        ctx.arc(centerX, centerY + bounce + 6, 12, 0.1 * Math.PI, 0.9 * Math.PI);
        ctx.strokeStyle = '#333';
        ctx.lineWidth = 2;
        ctx.stroke();
      }
    }

    requestAnimationFrame(drawFrame);
  }

  function drawStaticAvatar() {
    if (!ctx) { return; }
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    const centerX = canvas.width / 2;
    const centerY = canvas.height / 2;

    // Body
    ctx.beginPath();
    ctx.arc(centerX, centerY, 40, 0, Math.PI * 2);
    ctx.fillStyle = '#4caf50';
    ctx.fill();

    // Eyes
    ctx.fillStyle = '#fff';
    ctx.beginPath();
    ctx.arc(centerX - 12, centerY - 8, 6, 0, Math.PI * 2);
    ctx.arc(centerX + 12, centerY - 8, 6, 0, Math.PI * 2);
    ctx.fill();

    // Pupils
    ctx.fillStyle = '#333';
    ctx.beginPath();
    ctx.arc(centerX - 12, centerY - 8, 3, 0, Math.PI * 2);
    ctx.arc(centerX + 12, centerY - 8, 3, 0, Math.PI * 2);
    ctx.fill();

    // Smile
    ctx.beginPath();
    ctx.arc(centerX, centerY + 6, 12, 0.1 * Math.PI, 0.9 * Math.PI);
    ctx.strokeStyle = '#333';
    ctx.lineWidth = 2;
    ctx.stroke();
  }

  // --- Chat ---
  function addChatMessage(text, sender) {
    if (!chatMessages) { return; }
    const div = document.createElement('div');
    div.className = 'chat-msg ' + sender;
    div.textContent = text;
    div.setAttribute('role', 'article');
    chatMessages.appendChild(div);
    chatMessages.scrollTop = chatMessages.scrollHeight;
  }

  if (chatForm) {
    chatForm.addEventListener('submit', function (e) {
      e.preventDefault();
      var text = chatInput.value.trim();
      if (!text) { return; }
      addChatMessage(text, 'user');
      chatInput.value = '';
      vscode.postMessage({ type: 'chat:send', payload: text });
    });
  }

  // --- Controls ---
  if (btnPause) {
    btnPause.addEventListener('click', function () {
      vscode.postMessage({ type: 'animation:control', payload: { action: 'pause' } });
    });
  }

  // --- Message handling from extension ---
  window.addEventListener('message', function (event) {
    var message = event.data;
    switch (message.type) {
      case 'state:init':
      case 'state:update':
        state = Object.assign({}, state, message.payload);
        updateUI();
        break;
      case 'chat:response':
        addChatMessage(message.payload.text, 'agent');
        break;
      case 'chat:error':
        addChatMessage('Erreur: ' + message.payload.error, 'agent');
        break;
      case 'avatar:change':
        state.avatar = message.payload.avatar;
        break;
    }
  });

  function updateUI() {
    if (statusText) {
      statusText.textContent = state.chatLoading ? 'Reflexion...'
        : state.paused ? 'En pause'
        : state.running ? 'Actif'
        : 'Arrete';
    }
    if (statusIndicator) {
      statusIndicator.className = 'indicator ' + (
        state.chatLoading ? 'loading'
        : state.running ? 'active'
        : 'idle'
      );
    }
    if (btnSpeed) {
      btnSpeed.textContent = state.speed + 'x';
    }
    if (btnPause) {
      btnPause.textContent = state.paused ? 'Reprendre' : 'Pause';
    }
  }

  // --- Init ---
  vscode.postMessage({ type: 'ui:ready' });
  requestAnimationFrame(drawFrame);
})();
