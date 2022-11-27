import os 
import json

def create_instance():
    terraform_file = open("variables.tf.json", "r")
    data = json.load(terraform_file)
    terraform_file.close()

    name = input("\nInsira o nome da instância: ")
    print("\nTipos de instâncias disponíveis: ")
    print("1 - t2.micro")
    print("2 - t2.small")

    output = input("\nInsira o valor desejado: ")
    
    data["variable"]["instance_name"]["default"].append(name)
    if output == "1":
        data["variable"]["instance_type"]["default"].append("t2.micro")
    elif output == "2":
        data["variable"]["instance_type"]["default"].append("t2.small")

    sg = get_sg_id()
    if sg == None:
        data["variable"]["sg_instance"]["default"].append(sg)
    else:
        data["variable"]["sg_instance"]["default"].append([sg])


    terraform_file = open("variables.tf.json", "w")
    json.dump(data, terraform_file)
    terraform_file.close()

    os.system("terraform init")
    os.system("terraform plan")
    os.system("terraform apply -auto-approve")

def destroy_instance():
    terraform_file = open("variables.tf.json", "r")
    data = json.load(terraform_file)

    terraform_file.close()
    print("\nInstâncias disponíveis: ")
    for i in range(len(data["variable"]["instance_name"]["default"])):
        print(data["variable"]["instance_name"]["default"][i])
    deletar = input("\nInsira o nome da instância que deseja destruir: ")
    for i in range(len(data["variable"]["instance_name"]["default"])):
        if data["variable"]["instance_name"]["default"][i] == deletar:
            data["variable"]["instance_name"]["default"].pop(i)
            data["variable"]["instance_type"]["default"].pop(i)
            break
    terraform_file = open("variables.tf.json", "w")
    json.dump(data, terraform_file)
    terraform_file.close()

    os.system("terraform init")
    os.system("terraform plan")
    os.system("terraform apply -auto-approve")


def create_vpc():
    terraform_file = open("variables.tf.json", "r")
    data = json.load(terraform_file)
    terraform_file.close()

    name = input("\nInsira o nome da VPC: ")
    
    data["variable"]["vpc_name"]["default"].append(name)

    terraform_file = open("variables.tf.json", "w")
    json.dump(data, terraform_file)
    terraform_file.close()

    os.system("terraform init")
    os.system("terraform plan")
    os.system("terraform apply -auto-approve")

def create_user():
    terraform_file = open("variables.tf.json", "r")
    data = json.load(terraform_file)
    terraform_file.close()

    name = input("\nInsira o nome do usuário: ")
    
    data["variable"]["user_name"]["default"].append(name)

    terraform_file = open("variables.tf.json", "w")
    json.dump(data, terraform_file)
    terraform_file.close()

    os.system("terraform init")
    os.system("terraform plan")
    os.system("terraform apply -auto-approve")

def destroy_user():
    terraform_file = open("variables.tf.json", "r")
    data = json.load(terraform_file)

    terraform_file.close()
    print("\nUsuários disponíveis: \n")
    for i in range(len(data["variable"]["user_name"]["default"])):
        print(data["variable"]["user_name"]["default"][i])
    deletar = input("\nInsira o nome do usuário que deseja destruir: ")
    for i in range(len(data["variable"]["user_name"]["default"])):
        if data["variable"]["user_name"]["default"][i] == deletar:
            data["variable"]["user_name"]["default"].pop(i)
            break
    terraform_file = open("variables.tf.json", "w")
    json.dump(data, terraform_file)
    terraform_file.close()

    os.system("terraform init")
    os.system("terraform plan")
    os.system("terraform apply -auto-approve")

def create_sg():
    terraform_file = open("variables.tf.json", "r")
    data = json.load(terraform_file)
    terraform_file.close()

    name = input("\nInsira o nome do SG: ")
    
    data["variable"]["sg_name"]["default"].append(name)

    terraform_file = open("variables.tf.json", "w")
    json.dump(data, terraform_file)
    terraform_file.close()

    os.system("terraform init")
    os.system("terraform plan")
    os.system("terraform apply -auto-approve")

def destroy_sg():
    terraform_file = open("variables.tf.json", "r")
    data = json.load(terraform_file)

    terraform_file.close()
    print("\nSecurity Groups disponíveis: ")
    for i in range(len(data["variable"]["sg_name"]["default"])):
        print(data["variable"]["sg_name"]["default"][i])
    deletar = input("Insira o nome do Security Group que deseja destruir: ")
    for i in range(len(data["variable"]["sg_name"]["default"])):
        if data["variable"]["sg_name"]["default"][i] == deletar:
            data["variable"]["sg_name"]["default"].pop(i)
            break
    terraform_file = open("variables.tf.json", "w")
    json.dump(data, terraform_file)
    terraform_file.close()

    os.system("terraform init")
    os.system("terraform plan")
    os.system("terraform apply -auto-approve")


# def list_instances_users_sg_vpc():
#     terraform_file = open("variables.tf.json", "r")
#     data = json.load(terraform_file)
#     terraform_file.close()
#     print("\nInstâncias disponíveis: ")
#     for i in range(len(data["variable"]["instance_name"]["default"])):
#         print(data["variable"]["instance_name"]["default"][i])
#     print("\nUsuários disponíveis: ")
#     for i in range(len(data["variable"]["user_name"]["default"])):
#         print(data["variable"]["user_name"]["default"][i])
#     print("\nSecurity Groups disponíveis: ")
#     for i in range(len(data["variable"]["sg_name"]["default"])):
#         print(data["variable"]["sg_name"]["default"][i])
#     print("\nVPCs disponíveis: ")
#     for i in range(len(data["variable"]["vpc_name"]["default"])):
#         print(data["variable"]["vpc_name"]["default"][i])

#listar instancias, usuarios, sg e vpc com terraform.tfstate
def list_instances_users_sg_vpc():
    terraform_file = open("terraform.tfstate", "r")
    data = json.load(terraform_file)
    terraform_file.close()
    print("\nInstâncias disponíveis: ")
    for i in range(len(data["resources"])):
        if data["resources"][i]["type"] == "aws_instance":
            for j in range(len(data["resources"][i]["instances"])):
                print(data["resources"][i]["instances"][j]["attributes"]["tags"]["Name"], " - ", data["resources"][i]["instances"][j]["attributes"]["instance_type"], " - ",data["resources"][i]["instances"][j]["attributes"]["availability_zone"])
    print("\nUsuários disponíveis: ")
    for i in range(len(data["resources"])):
        if data["resources"][i]["type"] == "aws_iam_user":
            for j in range(len(data["resources"][i]["instances"])): 
                print(data["resources"][i]["instances"][j]["attributes"]["name"])
    print("\nSecurity Groups disponíveis: ")
    for i in range(len(data["resources"])):
        if data["resources"][i]["type"] == "aws_security_group":
            for j in range(len(data["resources"][i]["instances"])): 
                print(data["resources"][i]["instances"][j]["attributes"]["name"])
    print("\nVPCs disponíveis: ")
    for i in range(len(data["resources"])):
        if data["resources"][i]["type"] == "aws_vpc":
            for j in range(len(data["resources"][i]["instances"])):
                print(data["resources"][i]["instances"][j]["attributes"]["tags"]["Name"])


def get_sg_id():
    terraform_file = open("terraform.tfstate", "r")
    data = json.load(terraform_file)
    terraform_file.close()
    print("\nSecurity Groups disponíveis: ")
    for i in range(len(data["resources"])):
        if data["resources"][i]["type"] == "aws_security_group":
            for j in range (len(data["resources"][i]["instances"])):
                print(data["resources"][i]["instances"][j]["attributes"]["name"])
    sg = input("\nInsira o nome do Security Group que deseja associar: ")
    for i in range(len(data["resources"])):
        if data["resources"][i]["type"] == "aws_security_group":
            if data["resources"][i]["instances"][0]["attributes"]["name"] == sg:
                return data["resources"][i]["instances"][0]["attributes"]["id"]
    return None



def delete_all():
    terraform_file = open("variables.tf.json", "r")
    data = json.load(terraform_file)
    terraform_file.close()
    data["variable"]["instance_name"]["default"] = []
    data["variable"]["instance_type"]["default"] = []
    data["variable"]["vpc_name"]["default"] = []
    data["variable"]["user_name"]["default"] = []
    data["variable"]["sg_name"]["default"] = []
    data["variable"]["sg_instance"]["default"] = []
    terraform_file = open("variables.tf.json", "w")
    json.dump(data, terraform_file)
    terraform_file.close()

    os.system("terraform destroy -auto-approve")

def main():
    while True:
        print("\nBem vindo ao menu de criação de instâncias")
        print("1 - Criar instância")
        print("2 - Criar VPC")
        print("3 - Criar usuário")
        print("4 - Criar Security Group")
        print("5 - Destruir instância")
        print("6 - Deletar usuário")
        print("7 - Destruir Security Group")
        print("8 - Listar instâncias")
        print("9 - Destruir tudo")
        print("0 - Sair")
        opcao = input("Insira a opção desejada: \n")
        if opcao == "1":
            create_instance()
        elif opcao == "2":
            create_vpc()
        elif opcao == "3":
            create_user()
        elif opcao == "4":
            create_sg()
        elif opcao == "5":
            destroy_instance()
        elif opcao == "6":
            destroy_user()
        elif opcao == "7":
            destroy_sg()
        elif opcao == "8":
            list_instances_users_sg_vpc()
        elif opcao == "9":
            delete_all()
        elif opcao == "0":
            break
        else:
            print("Opção inválida")

main()