from crud.base_crud import BaseCrud
from crud.client_crud import ClientCrud
from models.company_model import CompanyModel
from repository.company_repository import CompanyRepository
from ui.menu import Menu
from ui.style import Style


class CompanyCrud(BaseCrud):
    def __init__(self):
        super().__init__('Companies', CompanyRepository(), CompanyModel())

    def make_paginated_data(self, limit, page):
        return {"data": self.repository.find_paginated(limit=limit, page=page),
                "headers": self.repository.get_headers()}

    def edit(self):
        print(Style.create_title('Edit Company'))
        company = Menu.pagination_menu(self.repository)
        if company:
            name = self.update_field(company['name'], 'Name')
            address = self.update_field(company['address'], 'Address')
            self.repository.update(company['id'], {'name': name, 'address': address})
            self.repository.save()
            self.repository.check_rows_updated('Company Updated')
        else:
            print('No changes made')
        Menu.wait_for_input()

    def delete(self):
        print(Style.create_title('Delete Company'))
        company = Menu.pagination_menu(self.repository)
        if company:
            user_action = False
            while not user_action == 'delete':
                user_action = input(
                    'Type \'delete\' to remove this company and ALL associated data or \'c\' to cancel: ')
                if user_action == 'c':
                    return
            if user_action == 'delete':
                ClientCrud().delete_clients_by_company_id(company['id'])
                self.repository.remove(company['id'])
                self.repository.save()
                self.repository.check_rows_updated('Company Deleted')
                Menu.wait_for_input()
