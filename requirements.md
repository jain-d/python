# Core Entities for Initial IMS Implementation

Start with these five essential entities that form the backbone of any inventory management system:

## 1. Product
The central entity representing items we're tracking.

- Product ID (unique identifier)
- Name and description
- Category (simplified to just one category per product initially)
- Price information (cost and retail price)
- Minimum stock level (reorder threshold)

**Business Rules:**
Products must have unique identifiers
Retail price must be greater than cost price
Products cannot be deleted once created (only deactivated)

## 2. Inventory
Tracks the quantity and status of products.

- Product reference
- Quantity on hand
- Quantity reserved (for pending orders)
- Location identifier (simplified)

**Business Rules:**
Available quantity (on hand minus reserved) cannot go below zero
Inventory adjustments require reason codes
Every quantity change must be recorded as a transaction

## 3. Supplier
Companies that provide our products.

- Supplier ID
- Name and basic contact information
- Payment terms (simplified)

**Business Rules:**
Each product must be linked to at least one supplier
Suppliers must have valid contact information

## 4. Purchase Order
Represents orders placed to suppliers to acquire inventory.

- PO number
- Supplier reference
- Order date
- Expected delivery date
- Status (draft, submitted, received)
- Line items (product, quantity, price)

**Business Rules:**
POs cannot be modified after being submitted to suppliers
Receiving a PO automatically increases inventory quantities
POs must have at least one line item

## 5. Inventory Transaction
Records every movement or adjustment of inventory.

- Transaction ID
- Transaction type (receiving, adjustment, sale)
- Product reference
- Quantity (positive or negative)
- Timestamp
- Reference document (PO number, etc.)
- Reason code (for adjustments)

**Business Rules:**
Every inventory change must have a corresponding transaction
Transactions cannot be deleted or modified once created
All transactions must be attributable (initially simplified to just a transaction type)

## Key Relationships

Products are supplied by one or more Suppliers
Products have Inventory records
Purchase Orders contain multiple Product line items
Purchase Orders are linked to one Supplier
Inventory Transactions reference Products
Purchase Orders generate Inventory Transactions when received

This focused set of entities provides a perfect balance of simplicity and complexity:

You'll implement all four OOP principles:

**Encapsulation**: Managing inventory levels through controlled methods
**Inheritance**: Different transaction types with specialized behaviors
**Polymorphism**: Processing different types of inventory movements
**Abstraction**: Separating business logic from data storage


### Real business challenges:

Maintaining data integrity (inventory never below zero)
Managing state transitions (PO statuses)
Enforcing business rules (transactions must balance)
Creating audit trails (immutable transaction history)
