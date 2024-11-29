import unittest
from connection import Connection
import tests as test

# coverage run -m pytest
# coverage report

# параметризированные тесты
# проверить все поля продукта при добавлении
# схема продукта (из чего должен состоять параметр)

class ParametrizedTestCase(unittest.TestCase):
    pass

def generateAddTest(connection):
    def test(self):
        connection = Connection()
        jsonTest = connection.getJsonAfterAddProduct(test.TEST)
        self.assertEqual(connection.isStatus(jsonTest), True, "Wrong status")
    return test

class APITests(unittest.TestCase):
    def testAddProductSuccess(self):
        connection = Connection()
        jsonTest = connection.getJsonAfterAddProduct(test.TEST)
        textJSON = test.TEST
        textJSON["id"] = connection.getIdFromAddingProduct(jsonTest)
        self.assertEqual(connection.isStatus(jsonTest), True, "Wrong status")
        self.assertEqual(connection.checkProductById(textJSON["id"]), True, "The product has not been added")
        self.assertEqual(connection.checkAllLinesOfProduct(textJSON), False, "One of lines of product is wrong")
        connection.deleteProductAfterAdding(jsonTest)

    def testAddProductAlias(self):
        connection = Connection()
        jsonTest = connection.getJsonAfterAddProduct(test.TEST_ALIAS)
        textJSON = test.TEST_ALIAS
        textJSON["id"] = connection.getIdFromAddingProduct(jsonTest)
        self.assertEqual(connection.isStatus(jsonTest), True, "Wrong status")
        self.assertEqual(connection.checkProductById(textJSON["id"]), True, "The product has not been added")
        self.assertEqual(connection.checkProductLine(test.TEST_ALIAS_VALUE, "alias"), True, "The alias of product is false")
        connection.deleteProductAfterAdding(jsonTest)
    
    def testAddProductNullContent(self):
        connection = Connection()
        jsonTest = connection.getJsonAfterAddProduct(test.TEST_NULL_CONTENT)
        textJSON = test.TEST_NULL_CONTENT
        textJSON["id"] = connection.getIdFromAddingProduct(jsonTest)
        self.assertEqual(connection.isStatus(jsonTest), True, "Wrong status")
        self.assertEqual(connection.checkProductById(textJSON["id"]), True, "The product has not been added with null content")
        self.assertEqual(connection.checkAllLinesOfProduct(textJSON), False, "One of lines of product is wrong")
        connection.deleteProductAfterAdding(jsonTest)

    def testAddProductNullDescription(self):
        connection = Connection()
        jsonTest = connection.getJsonAfterAddProduct(test.TEST_NULL_DESCRIPTION)
        textJSON = test.TEST_NULL_DESCRIPTION
        textJSON["id"] = connection.getIdFromAddingProduct(jsonTest)
        self.assertEqual(connection.isStatus(jsonTest), True, "Wrong status")
        self.assertEqual(connection.checkProductById(textJSON["id"]), True, "The product has not been added with null description")
        self.assertEqual(connection.checkAllLinesOfProduct(textJSON), False, "One of lines of product is wrong")
        connection.deleteProductAfterAdding(jsonTest)

    def testAddProductNullKeywords(self):
        connection = Connection()
        jsonTest = connection.getJsonAfterAddProduct(test.TEST_NULL_KEYWORDS)
        textJSON = test.TEST_NULL_KEYWORDS
        textJSON["id"] = connection.getIdFromAddingProduct(jsonTest)
        self.assertEqual(connection.isStatus(jsonTest), True, "Wrong status")
        self.assertEqual(connection.checkProductById(textJSON["id"]), False, "The product has not been added with null keywords")
        self.assertEqual(connection.checkAllLinesOfProduct(textJSON), False, "One of lines of product is wrong")
        connection.deleteProductAfterAdding(jsonTest)

    def testAddProductWrongCategory(self):
        connection = Connection()
        jsonTest = connection.getJsonAfterAddProduct(test.TEST_WRONG_CATEGORY)
        textJSON = test.TEST_WRONG_CATEGORY
        textJSON["id"] = connection.getIdFromAddingProduct(jsonTest)
        self.assertEqual(connection.isStatus(jsonTest), True, "Wrong status")
        self.assertEqual(connection.checkProductById(textJSON["id"]), False, "The product has been added with wrong category")
        connection.deleteProductAfterAdding(jsonTest)

    def testAddProductWrongHit(self):
        connection = Connection()
        jsonTest = connection.getJsonAfterAddProduct(test.TEST_WRONG_HIT)
        textJSON = test.TEST_WRONG_HIT
        textJSON["id"] = connection.getIdFromAddingProduct(jsonTest)
        self.assertEqual(connection.isStatus(jsonTest), True, "Wrong status")
        self.assertEqual(connection.checkProductById(textJSON["id"]), True, "The product has not been added with wrong hit")
        connection.deleteProductAfterAdding(jsonTest)
    
    def testAddProductWrongStatus(self):
        connection = Connection()
        jsonTest = connection.getJsonAfterAddProduct(test.TEST_WRONG_STATUS)
        self.assertEqual(connection.isStatus(jsonTest), True, "Wrong status")
        textJSON = test.TEST_WRONG_STATUS
        textJSON["id"] = connection.getIdFromAddingProduct(jsonTest)
        self.assertEqual(connection.checkProductById(textJSON["id"]), True, "The product has not been added with wrong status")
        connection.deleteProductAfterAdding(jsonTest)

    def testDeleteExistingProduct(self):
        connection = Connection()
        json = connection.getJsonAfterAddProduct(test.TEST) 
        id = connection.getIdFromAddingProduct(json)
        jsonTest = connection.getJsonAfterDeleteProduct(id)
        self.assertEqual(connection.isStatus(jsonTest), True, "Wrong status")
        self.assertEqual(connection.checkProductById(id), False, "The product has not been deleted")

    def testDeleteNonExistingProduct(self):
        connection = Connection()
        jsonTest = connection.getJsonAfterDeleteProduct(test.ID_PRODUCT_TEST)
        self.assertEqual(connection.isStatus(jsonTest), False, "The product has been deleted when it is not existing")

    def testEditTitleProduct(self):
        connection = Connection()
        json = connection.getJsonAfterAddProduct(test.TEST) 
        textJSON = test.NEW_TEST_TITLE
        textJSON["id"] = connection.getIdFromAddingProduct(json)
        jsonTest = connection.getJsonAfterEditProduct(test.NEW_TEST_TITLE)
        self.assertEqual(connection.isStatus(jsonTest), True, "Wrong status")
        self.assertEqual(connection.checkProductLine(textJSON, "title"), False, "The title of product has not been edited")
        connection.deleteProductAfterAdding(json)

    def testEditCategoryProduct(self):
        connection = Connection()
        json = connection.getJsonAfterAddProduct(test.TEST) 
        textJSON = test.NEW_TEST_CATEGORY_ID
        textJSON["id"] = connection.getIdFromAddingProduct(json)
        jsonTest = connection.getJsonAfterEditProduct(test.NEW_TEST_CATEGORY_ID)
        self.assertEqual(connection.isStatus(jsonTest), True, "Wrong status")
        self.assertEqual(connection.checkProductLine(textJSON, "category_id"), True, "The category_id of product has not been edited")
        connection.deleteProductAfterAdding(json)

    def testEditStatusProduct(self):
        connection = Connection()
        json = connection.getJsonAfterAddProduct(test.TEST) 
        textJSON = test.NEW_TEST_STATUS
        textJSON["id"] = connection.getIdFromAddingProduct(json)
        jsonTest = connection.getJsonAfterEditProduct(test.NEW_TEST_STATUS)
        self.assertEqual(connection.isStatus(jsonTest), True, "Wrong status")
        self.assertEqual(connection.checkProductLine(textJSON, "status"), True, "The status of product has not been edited")
        connection.deleteProductAfterAdding(json)

    def testEditWrongStatusProduct(self):
        connection = Connection()
        json = connection.getJsonAfterAddProduct(test.TEST) 
        textJSON = test.NEW_TEST_WRONG_STATUS
        textJSON["id"] = connection.getIdFromAddingProduct(json)
        jsonTest = connection.getJsonAfterEditProduct(test.NEW_TEST_WRONG_STATUS)
        self.assertEqual(connection.isStatus(jsonTest), True, "Wrong status")
        self.assertEqual(connection.checkProductLine(textJSON, "status"), False, "The status of product has been edited with wrong status")
        connection.deleteProductAfterAdding(json)

    def testEditContentProduct(self):
        connection = Connection()
        json = connection.getJsonAfterAddProduct(test.TEST) 
        textJSON = test.NEW_TEST_CONTENT
        textJSON["id"] = connection.getIdFromAddingProduct(json)
        jsonTest = connection.getJsonAfterEditProduct(test.NEW_TEST_CONTENT)
        self.assertEqual(connection.isStatus(jsonTest), True, "Wrong status")
        self.assertEqual(connection.checkProductLine(textJSON, "content"), True, "The content of product has not been edited")
        connection.deleteProductAfterAdding(json)

    def testEditPriceProduct(self):
        connection = Connection()
        json = connection.getJsonAfterAddProduct(test.TEST) 
        textJSON = test.NEW_TEST_PRICE
        textJSON["id"] = connection.getIdFromAddingProduct(json)
        jsonTest = connection.getJsonAfterEditProduct(test.NEW_TEST_PRICE)
        self.assertEqual(connection.isStatus(jsonTest), True, "Wrong status")
        self.assertEqual(connection.checkProductLine(textJSON, "price"), True, "The price of product has not been edited")
        connection.deleteProductAfterAdding(json)

    def testEditOldPriceProduct(self):
        connection = Connection()
        json = connection.getJsonAfterAddProduct(test.TEST) 
        textJSON = test.NEW_TEST_OLD_PRICE
        textJSON["id"] = connection.getIdFromAddingProduct(json)
        jsonTest = connection.getJsonAfterEditProduct(test.NEW_TEST_OLD_PRICE)
        self.assertEqual(connection.isStatus(jsonTest), True, "Wrong status")
        self.assertEqual(connection.checkProductLine(textJSON, "old_price"), True, "The old_price of product has not been edited")
        connection.deleteProductAfterAdding(json)

    def testEditKeywordsProduct(self):
        connection = Connection()
        json = connection.getJsonAfterAddProduct(test.TEST) 
        textJSON = test.NEW_TEST_KEYWORDS
        textJSON["id"] = connection.getIdFromAddingProduct(json)
        jsonTest = connection.getJsonAfterEditProduct(test.NEW_TEST_KEYWORDS)
        self.assertEqual(connection.isStatus(jsonTest), True, "Wrong status")
        self.assertEqual(connection.checkProductLine(textJSON, "keywords"), True, "The keywords of product has not been edited")
        connection.deleteProductAfterAdding(json)

    def testEditDescriptionProduct(self):
        connection = Connection()
        json = connection.getJsonAfterAddProduct(test.TEST) 
        textJSON = test.NEW_TEST_DESCRIPTION
        textJSON["id"] = connection.getIdFromAddingProduct(json)
        jsonTest = connection.getJsonAfterEditProduct(test.NEW_TEST_DESCRIPTION)
        self.assertEqual(connection.isStatus(jsonTest), True, "Wrong status")
        self.assertEqual(connection.checkProductLine(textJSON, "description"), FAlse, "The description of product has not been edited")
        connection.deleteProductAfterAdding(json)

    def testEditHitProduct(self):
        connection = Connection()
        json = connection.getJsonAfterAddProduct(test.TEST) 
        textJSON = test.NEW_TEST_HIT
        textJSON["id"] = connection.getIdFromAddingProduct(json)
        jsonTest = connection.getJsonAfterEditProduct(test.NEW_TEST_HIT)
        self.assertEqual(connection.isStatus(jsonTest), True, "Wrong status")
        self.assertEqual(connection.checkProductLine(textJSON, "hit"), True, "The hit of product has not been edited")
        connection.deleteProductAfterAdding(json)

    def testEditWrongHitProduct(self):
        connection = Connection()
        json = connection.getJsonAfterAddProduct(test.TEST) 
        textJSON = test.NEW_TEST_WRONG_HIT
        textJSON["id"] = connection.getIdFromAddingProduct(json)
        jsonTest = connection.getJsonAfterEditProduct(test.NEW_TEST_WRONG_HIT)
        self.assertEqual(connection.isStatus(jsonTest), True, "Wrong status")
        self.assertEqual(connection.checkProductLine(textJSON, "hit"), False, "The hit of product has been edited with wrong hit")
        connection.deleteProductAfterAdding(json)
        

if __name__ == "__main__":
    unittest.main()
