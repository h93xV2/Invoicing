from repository.base_repository import BaseRepository


class ClientRepository(BaseRepository):
    def find_clients(self):
        self.cursor.execute('select id, fullname, email, telephone, telephone from clients')
        return self.get_all()

    def find_client_by_id(self, id):
        self.cursor.execute('select id, fullname, email, telephone from clients where id = ?', (id,))
        return self.get_one()

    def find_client_by_company_id(self, company_id):
        self.cursor.execute('select id, fullname, email, telephone from clients where company_id = ?', (company_id,))
        return self.get_one()

    def find_client_and_company_by_id(self, id):
        self.cursor.execute('select id, fullname, email, telephone, name, address from clients join company on client.company_id = company.id where client.id = ?', (id,))
        return self.get_one()

    def insert_client(self, fullname, email, telephone):
        self.cursor.execute('insert into clients (fullname, email, telephone) values (?, ?)', (fullname, email, telephone))

    def update_client(self, id, fullname, email, telephone):
        self.cursor.execute('update clients set fullname = ?, email = ? where id = ?', (fullname, email, telephone, id))

    def remove_client(self, id):
        self.cursor.execute('delete from clients where id = ?', (id,))