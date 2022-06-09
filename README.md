# Inventory System Functions


### _**Suppliers**_

> **Add**
  - Name
  - Address
  
> **Update**
  - Name
  - Address
  
> **Delete Suppliers** (On-Going)

    - The user can **on delete cascade** ( which deletes all rows of orders referencing this product ) 
    - Or the user can  **on delete set null** ( which set all the foreign keys of referencing rows to null )

### _**Customers**_

> **Add**
  - First, Middle, Lastname
  - Address
  - Date Added
  
> **Update**
  - First, Middle, Lastname
  - Address

> **Delete Customers** (On-Going)

    - The user can **on delete cascade** ( which deletes all rows of orders referencing this product ) 
    - Or the user can  **on delete set null** ( which set all the foreign keys of referencing rows to null )


### _**Products**_

> **Add**
  - Upload Product Image (To Be Implemented)
  - Supplier (Existing Supplier) (On-going) (Drop-down)
  - Product Name
  - Cost (Per Piece)
  - Price (SRP)
  - Variant
  - Category
  - Inventory Received (Initial Inventory)
  - Minimum Required (For Checking and Alerts)

> **Update**
  - Supplier (Existing Supplier) (On-going) (Drop-down) (locked / Not-Editable)
  - Product Name
  - Cost (Per Piece)
  - Price (SRP)
  - Variant
  - Category
  
  - Inventory On Hand ( Deduct or Add ) ( _Disabling this field is possible because the user must not be able to add or subtract to the inventory because the user must do it in PURCHASES or ORDERS Page._)
    - When Deducting the purchases and on hand is affected ( Deduction )
    - When Adding the purchases and on hand is affected ( Addition )
    
  - Minimum Required (For Checking and Alerts) 

> **Delete**

  - When a product is Deleted
  
    - User Must Choose Either
      - The user can **on delete cascade** ( which deletes all rows of purchases and orders referencing this product ) 
      - Or the user can  **on delete set null** ( which set all the foreign keys of referencing rows to null )


### _**Purchases**_ (On Going)

> **add**
  - _Amount of Purchased product will be Added to the TOTAL PURCHASED and ON HAND_
  - 
> **update**
  - _If the Amount Purchased is Updated Then the amount will reflect to TOTAL PURCHASED and ON HAND_
  - 
> **delete**
  - _If the Amount Purchased is Deleted Then the amount will reflect to TOTAL PURCHASED and ON HAND_
  - 

### _**Orders**_ (On Going)

> **add**
  - _Amount of Ordered product will be Added to the TOTAL Ordered and  deduct to inventory ON HAND_
> **update**
  -_If the Amount Ordered is Updated Then the amount will reflect to TOTAL PURCHASED and ON HAND_
> **delete**
  -_If the Amount Ordered is Deleted Then the amount will reflect to TOTAL PURCHASED and ON HAND_

## SEARCH

## DASHBOARD

## GENERATE REPORT
