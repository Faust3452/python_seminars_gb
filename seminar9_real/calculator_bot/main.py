import UI
import app_logger

app_logger.bot_start()
try:
    UI.user_interface()
except Exception as e:
    app_logger.emergency_exit()