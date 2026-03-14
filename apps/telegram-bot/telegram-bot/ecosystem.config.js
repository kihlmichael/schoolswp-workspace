// pm2 ecosystem config — ccpa-telegram bot
module.exports = {
  apps: [
    {
      name: "claude-telegram-bot",
      script: "node_modules/ccpa-telegram/dist/index.js",
      cwd: "/root/workspace/telegram-bot",
      env_file: ".env",
      restart_delay: 5000,
      max_restarts: 10,
      watch: false,
      log_date_format: "YYYY-MM-DD HH:mm:ss",
      out_file: "/root/logs/bot-out.log",
      error_file: "/root/logs/bot-err.log"
    }
  ]
}
