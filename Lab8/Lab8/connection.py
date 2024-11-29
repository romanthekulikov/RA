import requests as req
import settings as setting

class Connection:
    def getJson(self, url):
        response = req.get(url)
        return response.json()
    
    def postJson(self, url, data):
        response = req.post(url, json=data)
        return response.json()
    
    def isStatus(self, json):
        if json['status'] != 0:
            return True
        return False

    def getJsonAfterAddProduct(self, data):
        return self.postJson(setting.ADD_PRODUCT, data)

    def getJsonAfterDeleteProduct(self, idProduct = int()):
        return self.getJson(setting.DELETED_PRODUCT + str(idProduct))
    
    def getJsonAfterEditProduct(self, data):
        return self.postJson(setting.EDIT_PRODUCT, data)
    
    def getIdFromAddingProduct(self, response):
        if self.isStatus(response):
            return response['id']
        return ""

    def deleteProductAfterAdding(self, response):
        if self.isStatus(response): 
            self.getJsonAfterDeleteProduct(self.getIdFromAddingProduct(response))
        return False

    def checkProductById(self, checkProductId):
        response = req.get(setting.LIST_OF_PRODUCTS)
        listOfProducts = response.json()
        # print(checkProduct["id"], listOfProducts[len(listOfProducts) - 1]["id"])
        if str(checkProductId) == str(listOfProducts[len(listOfProducts) - 1]["id"]):
            return True
        return False
    
    # def checkProductLine(self, checkProduct, product, line):
    #     if str(checkProduct[line]) == str(product[line]):
    #         print(str(checkProduct[line]), str(product[line]))
    #         return True
    #     return False
    
    def checkProductLine(self, checkProduct, line):
        response = req.get(setting.LIST_OF_PRODUCTS)
        listOfProducts = response.json()
        if str(checkProduct[line]) == str(listOfProducts[len(listOfProducts) - 1][line]):
            return True
        return False
    
    def checkAllLinesOfProduct(self, checkProduct):
        response = req.get(setting.LIST_OF_PRODUCTS)
        listOfProducts = response.json()
        product = listOfProducts[len(listOfProducts) - 1]
        for line in checkProduct.keys():
            if line in product.keys():
                #print(str(checkProduct[line]), str(product[line]))
                if str(checkProduct[line]) == str(product[line]):
                    continue
                    #print(str(checkProduct[line]), str(product[line]))
                else:
                    return False
        return True
        # if str(checkProduct[]) == str(listOfProducts[len(listOfProducts) - 1][line]):
        #     return True
    
    # def generateNewId(self):
    #     response = req.get(setting.LIST_OF_PRODUCTS)
    #     listOfProsucts = response.json()
    #     return len(listOfProsucts)
        
connection = Connection()
print(connection.getJsonAfterDeleteProduct(31781))

