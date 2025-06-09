from multiprocessing import Process

def rodar_interface_crianca():
    import refeicao_crianca

def rodar_interface_cozinha():
    import refeicao_cozinha

if __name__ == "__main__":
    p1 = Process(target=rodar_interface_crianca)
    p2 = Process(target=rodar_interface_cozinha)

    p1.start()
    p2.start()

    p1.join()
    p2.join()

