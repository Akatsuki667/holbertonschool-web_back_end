# NoSQL

## 0. List all databases
- Write a script that lists all databases in MongoDB.

## 1. Create a database
Write a script that creates or uses the database `my_db`:

## 2. Insert document
- Write a script that inserts a document in the collection `school`:
    - The document must have one attribute `name` with value “Holberton school”
    - The database name will be passed as option of `mongo` command

## 3. All documents
- Write a script that lists all documents in the collection `school`:
    - The database name will be passed as option of `mongo` command

## 4. All matches
- Write a script that lists all documents with `name="Holberton school"` in the collection `school`:
    - The database name will be passed as option of `mongo` command

## 5. Count
- Write a script that displays the number of documents in the collection `school`:
    - The database name will be passed as option of `mongo` command

## 6. Update
- Write a script that adds a new attribute to a document in the collection `school`:
    - The script should update only document with `name="Holberton school"` (all of them)
    - The update should add the attribute `address` with the value “972 Mission street”
    - The database name will be passed as option of `mongo` command

## 7. Delete by match
- Write a script that deletes all documents with `name="Holberton school"` in the collection `school`:
    - The database name will be passed as option of `mongo` command

## 8. List all documents in Python
 Write a Python function that lists all documents in a collection:
    - Prototype: `def list_all(mongo_collection):`
    - Return an empty list if no document in the collection
    - `mongo_collection` will be the `pymongo` collection object

