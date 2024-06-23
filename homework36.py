import multiprocessing


class WarehouseManager:
    def __init__(self):
        self.data = {}

    def process_request(self, request, conn):

        for req in request:
            if req.count('receipt'):
                self.data.update({req[0]: req[2]})
            if req.count('shipment'):
                if (self.data.get(req[0]) != None) and (self.data.get(req[0]) > 0):
                    new_data = self.data.get(req[0]) - req[2]
                    self.data.update({req[0]: new_data})
        conn.send(self.data)
        conn.close()

    def run(self, requ):
        data_in, data_out = multiprocessing.Pipe()
        pr = multiprocessing.Process(target=self.process_request, args=(requ, data_in))
        pr.start()
        pr.join()
        self.data = data_out.recv()


if __name__ == '__main__':
    manager = WarehouseManager()

    requests = [
        ("product1", "receipt", 100),
        ("product2", "receipt", 150),
        ("product1", "shipment", 30),
        ("product3", "receipt", 200),
        ("product2", "shipment", 50)
    ]

    manager.run(requests)
    print(manager.data)
