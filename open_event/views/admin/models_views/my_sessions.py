from flask_admin import BaseView, expose
from ....helpers.data_getter import DataGetter

class MySessionView(BaseView):

    @expose('/')
    def display_my_sessions_view(self):
        return self.render('/gentelella/admin/scheduler/scheduler.html')

    @expose('/<session_id>')
    def display_session_view(self, session_id):
        return self.render('/gentelella/admin/scheduler/scheduler.html')
