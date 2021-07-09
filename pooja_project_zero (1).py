#!/usr/bin/env python
# coding: utf-8

# In[77]:


# Importing packages
import pymongo
from pymongo import MongoClient


# In[78]:


# Connection to MongoDB instance
Client = pymongo.MongoClient("localhost",27017)


# In[79]:


# For creating a database
Database = Client["project_zero"]


# In[80]:


# For creating a collection
Collection = Database["meal_info"]


# In[73]:


# meal_info
Data = [{"meal_id":1885,"category":"Beverages","cuisine":"Thai"},{"meal_id":1993,"category":"Beverages","cuisine":"Thai"},{"meal_id":2539,"category":"Beverages","cuisine":"Thai"},{"meal_id":1248,"category":"Beverages","cuisine":"Indian"},{"meal_id":2631,"category":"Beverages","cuisine":"Indian"},{"meal_id":1311,"category":"Extras","cuisine":"Thai"},{"meal_id":1062,"category":"Beverages","cuisine":"Italian"},{"meal_id":1778,"category":"Beverages","cuisine":"Italian"},{"meal_id":1803,"category":"Extras","cuisine":"Thai"},{"meal_id":1198,"category":"Extras","cuisine":"Thai"},{"meal_id":2707,"category":"Beverages","cuisine":"Italian"},{"meal_id":1847,"category":"Soup","cuisine":"Thai"},{"meal_id":1438,"category":"Soup","cuisine":"Thai"},{"meal_id":2494,"category":"Soup","cuisine":"Thai"},{"meal_id":2760,"category":"Other Snacks","cuisine":"Thai"},{"meal_id":2490,"category":"Salad","cuisine":"Italian"},{"meal_id":1109,"category":"Rice Bowl","cuisine":"Indian"},{"meal_id":2290,"category":"Rice Bowl","cuisine":"Indian"},{"meal_id":1525,"category":"Other Snacks","cuisine":"Thai"},{"meal_id":2704,"category":"Other Snacks","cuisine":"Thai"},{"meal_id":1878,"category":"Starters","cuisine":"Thai"},{"meal_id":2640,"category":"Starters","cuisine":"Thai"},{"meal_id":2577,"category":"Starters","cuisine":"Thai"},{"meal_id":1754,"category":"Sandwich","cuisine":"Italian"},{"meal_id":1971,"category":"Sandwich","cuisine":"Italian"},{"meal_id":2306,"category":"Pasta","cuisine":"Italian"},{"meal_id":2139,"category":"Beverages","cuisine":"Indian"},{"meal_id":2826,"category":"Sandwich","cuisine":"Italian"},{"meal_id":2664,"category":"Salad","cuisine":"Italian"},{"meal_id":2569,"category":"Salad","cuisine":"Italian"},{"meal_id":1230,"category":"Beverages","cuisine":"Continental"},{"meal_id":1207,"category":"Beverages","cuisine":"Continental"},{"meal_id":2322,"category":"Beverages","cuisine":"Continental"},{"meal_id":2492,"category":"Desert","cuisine":"Indian"},{"meal_id":1216,"category":"Pasta","cuisine":"Italian"},{"meal_id":1727,"category":"Rice Bowl","cuisine":"Indian"},{"meal_id":1902,"category":"Biryani","cuisine":"Indian"},{"meal_id":1247,"category":"Biryani","cuisine":"Indian"},{"meal_id":2304,"category":"Desert","cuisine":"Indian"},{"meal_id":1543,"category":"Desert","cuisine":"Indian"},{"meal_id":1770,"category":"Biryani","cuisine":"Indian"},{"meal_id":2126,"category":"Pasta","cuisine":"Italian"},{"meal_id":1558,"category":"Pizza","cuisine":"Continental"},{"meal_id":2581,"category":"Pizza","cuisine":"Continental"},{"meal_id":1962,"category":"Pizza","cuisine":"Continental"},{"meal_id":1571,"category":"Fish","cuisine":"Continental"},{"meal_id":2956,"category":"Fish","cuisine":"Continental"},{"meal_id":2104,"category":"Fish","cuisine":"Continental"},{"meal_id":2444,"category":"Seafood","cuisine":"Continental"},{"meal_id":2867,"category":"Seafood","cuisine":"Continental"},{"meal_id":1445,"category":"Seafood","cuisine":"Continental"}]


# In[68]:


#For inserting the many records
result = Collection.insert_many(Data)


# In[81]:


# INSERTED_IDS
inserted_ids_value = result.inserted_ids

for i in inserted_ids_value:
    print(i)
    


# In[82]:


# For inserting the one record
record1 = {"meal_id":1998,"category":"Snacks","cuisine":"Indian"}
result1 = Collection.insert_one(record1)


# In[83]:


# For deleting the one record
Collection.delete_one({'_id':1993})


# In[84]:


# Sorting in ascending order
Result2 = Collection.find().sort("_id",1)

for i in Result2:
    print(i)


# In[85]:


# Sorting in descending order
Result3 = COLLECTION.find().sort("_id",-1)

for i in Result3:
    print(i)


# In[86]:


# For finding all the records 
result4=Collection.find()

for i in result4:
    print(i)


# In[87]:


# For finding the one record
Collection.find_one({"category":"Salad"})


# In[89]:


# For updating the many records
record2 = {'meal_id': 240, 'category': 'Snacks', 'cuisine': 'Italian'}
Collection.update_many({"meal_id":24},{"$set":record2})


# In[91]:


# For updating the one records
record3 = {'meal_id': 249, 'category': 'Snacks', 'cuisine': 'Italian'}
Collection.update_one({"meal_id":240},{"$set":record3})


# In[20]:


# For limiting the records
result_1 = Collection.find().limit(10)
for i in result_1:
    print(i)


# In[92]:


# For deleting many records
Collection.delete_many({})


# In[ ]:





# In[ ]:




