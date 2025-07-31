from django.apps import AppConfig
import dashboard.dash_apps.finished_apps.advanced_dash 


class DashboardConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'dashboard'

    def ready(self):
        import dashboard.dash_apps.finished_apps.first_dash
        import dashboard.dash_apps.finished_apps.advanced_dash
        
