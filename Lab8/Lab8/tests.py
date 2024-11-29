testCase = {
    "id": int(),
    "category_id": range(1,16),
    "title": str(),
    "alias": str(),
    "content": str(),
    "price": int(),
    "old_price": int(),
    "status": 0|1,
    "keywords": str(),
    "description": str(),
    "hit": 0|1,
}
ID_PRODUCT_TEST = 65
TEST =  {
    "id": "65",
    "category_id": "8",
    "title": "Harmony 41040-01",
    "alias": "harmony-41040-01-0-0-0-0-0",
    "content": "harmony",
    "price": "90",
    "old_price": "0",
    "status": "1",
    "keywords": "harmony",
    "description": "harmony",
    "hit": "1",
  }

TEST_ALIAS = {
    "id": "65",
    "category_id": "8",
    "title": "Alias Test 41040-01",
    "alias": "alias-test-41040-01",
    "content": "harmony",
    "price": "90",
    "old_price": "0",
    "status": "1",
    "keywords": "harmony",
    "description": "harmony",
    "hit": "1",
}

TEST_ALIAS_VALUE = {
    "alias": "alias-test-41040-01-0",
}

TEST_WRONG_CATEGORY =  {
    "id": "65",
    "category_id": "25",
    "title": "harmony 41040-01",
    "alias": "harmony-41040-01-0-0-0-0-0-0",
    "content": "harmony",
    "price": "90",
    "old_price": "0",
    "status": "45",
    "keywords": "harmony",
    "description": "harmony",
    "hit": "1",
  }

TEST_WRONG_HIT = {
    "id": "65",
    "category_id": "8",
    "title": "Harmony 41040-01",
    "alias": "harmony-41040-01-0-0-0-0-0",
    "content": "harmony",
    "price": "90",
    "old_price": "0",
    "status": "1",
    "keywords": "harmony",
    "description": "harmony",
    "hit": "2",
}

TEST_NULL_CONTENT = {
    "id": "65",
    "category_id": "8",
    "title": "Harmony 41040-01",
    "alias": "harmony-41040-01-0-0-0-0-0",
    "content": None,
    "price": "90",
    "old_price": "0",
    "status": "1",
    "keywords": "harmony",
    "description": "harmony",
    "hit": "1",
  }

TEST_NULL_KEYWORDS = {
    "id": "65",
    "category_id": "8",
    "title": "Harmony 41040-01",
    "alias": "harmony-41040-01-0-0-0-0-0",
    "content": "harmony",
    "price": "90",
    "old_price": "0",
    "status": "1",
    "keywords": None,
    "description": "harmony",
    "hit": "1",
  }

TEST_NULL_DESCRIPTION =  {
    "id": "65",
    "category_id": "8",
    "title": "Harmony 41040-01",
    "alias": "harmony-41040-01-0-0-0-0-0",
    "content": "harmony",
    "price": "90",
    "old_price": "0",
    "status": "1",
    "keywords": "harmony",
    "description": None,
    "hit": "1",
  }


TEST_WRONG_STATUS = {
    "id": "65",
    "category_id": "8",
    "title": "harmony 41040-01",
    "alias": "harmony-41040-01-0-0-0-0-0",
    "content": "harmony",
    "price": "90",
    "old_price": "0",
    "status": "45",
    "keywords": "harmony",
    "description": "harmony",
    "hit": "1",
  }

NEW_TEST_TITLE =   {
    "id": "65",
    "category_id": "8",
    "title": "New harmony 41040-01",
    "alias": "harmony-41040-01-0-0-0-0-0",
    "content": "harmony",
    "price": "90",
    "old_price": "0",
    "status": "1",
    "keywords": "harmony",
    "description": "harmony",
    "hit": "1",
  }

NEW_TEST_CATEGORY_ID =  {
    "id": "65",
    "category_id": "1",
    "title": "Harmony 41040-01",
    "alias": "harmony-41040-01-0-0-0-0-0",
    "content": "harmony",
    "price": "90",
    "old_price": "0",
    "status": "1",
    "keywords": "harmony",
    "description": "harmony",
    "hit": "1",
  }

NEW_TEST_WRONG_CATEGORY_ID =  {
    "id": "65",
    "category_id": "45",
    "title": "Harmony 41040-01",
    "alias": "harmony-41040-01-0-0-0-0-0",
    "content": "harmony",
    "price": "90",
    "old_price": "0",
    "status": "1",
    "keywords": "harmony",
    "description": "harmony",
    "hit": "1",
  }

NEW_TEST_STATUS =  {
    "id": "65",
    "category_id": "8",
    "title": "Harmony 41040-01",
    "alias": "harmony-41040-01-0-0-0-0-0",
    "content": "harmony",
    "price": "90",
    "old_price": "0",
    "status": "0",
    "keywords": "harmony",
    "description": "harmony",
    "hit": "1",
  }

NEW_TEST_WRONG_STATUS =  {
    "id": "65",
    "category_id": "8",
    "title": "Harmony 41040-01",
    "alias": "harmony-41040-01-0-0-0-0-0",
    "content": "harmony",
    "price": "90",
    "old_price": "0",
    "status": "36",
    "keywords": "harmony",
    "description": "harmony",
    "hit": "1",
  }

NEW_TEST_CONTENT =  {
    "id": "65",
    "category_id": "8",
    "title": "Harmony 41040-01",
    "alias": "harmony-41040-01-0-0-0-0-0",
    "content": "new harm",
    "price": "90",
    "old_price": "0",
    "status": "1",
    "keywords": "harmony",
    "description": "harmony",
    "hit": "1",
  }

NEW_TEST_PRICE = {
    "id": "65",
    "category_id": "8",
    "title": "Harmony 41040-01",
    "alias": "harmony-41040-01-0-0-0-0-0",
    "content": "harmony",
    "price": "300",
    "old_price": "0",
    "status": "1",
    "keywords": "harmony",
    "description": "harmony",
    "hit": "1",
  }

NEW_TEST_OLD_PRICE = {
    "id": "65",
    "category_id": "8",
    "title": "Harmony 41040-01",
    "alias": "harmony-41040-01-0-0-0-0-0",
    "content": "harmony",
    "price": "90",
    "old_price": "600",
    "status": "1",
    "keywords": "harmony",
    "description": "harmony",
    "hit": "1",
  }

NEW_TEST_KEYWORDS = {
    "id": "65",
    "category_id": "8",
    "title": "Harmony 41040-01",
    "alias": "harmony-41040-01-0-0-0-0-0",
    "content": "harmony",
    "price": "90",
    "old_price": "0",
    "status": "1",
    "keywords": "new harm",
    "description": "harmony",
    "hit": "1",
  }

NEW_TEST_DESCRIPTION = {
    "id": "65",
    "category_id": "8",
    "title": "Harmony 41040-01",
    "alias": "harmony-41040-01-0-0-0-0-0",
    "content": "harmony",
    "price": "90",
    "old_price": "0",
    "status": "1",
    "keywords": "harmony",
    "description": "new harm",
    "hit": "1",
  }

NEW_TEST_HIT = {
    "id": "65",
    "category_id": "8",
    "title": "Harmony 41040-01",
    "alias": "harmony-41040-01-0-0-0-0-0",
    "content": "harmony",
    "price": "90",
    "old_price": "0",
    "status": "1",
    "keywords": "harmony",
    "description": "harmony",
    "hit": "0",
  }

NEW_TEST_WRONG_HIT = {
    "id": "65",
    "category_id": "8",
    "title": "Harmony 41040-01",
    "alias": "harmony-41040-01-0-0-0-0-0",
    "content": "harmony",
    "price": "90",
    "old_price": "0",
    "status": "1",
    "keywords": "harmony",
    "description": "harmony",
    "hit": "2",
  }