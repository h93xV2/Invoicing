from actions.action_collection import ActionCollection
from crud.base_crud import BaseCrud
from crud.job_crud import JobCrud
from models.staff_model import StaffModel
from repository.staff_repository import StaffRepository
from ui.menu import Menu


# Todo: show jobs assigned to staff member
# Todo: Log time against staff members jobs
class StaffCrud(BaseCrud):
    def __init__(self):
        super().__init__('Staff', StaffRepository, StaffModel)

    def show_item_menu(self, id):
        Menu.create(self.table_name + 'Menu', ActionCollection(
            ('Show Assigned Jobs', lambda: JobCrud().show_jobs_by_assigned_to(id)),
        ))
