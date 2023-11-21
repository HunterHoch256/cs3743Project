# Ideas
- A report query that uses a JOIN (any type) to report on some aggregate value based on a group by clause.
    - Report the number of open service tickets, and group by hazardous/fragile status
- A query that includes a subquery.
    - Create a FORMEREMPLOYEES table, with data from the EMPLOYEES table, though with some sensitive values removed (e.g., SSN, address)
- A query that creates a view.
- A query that demonstrates the view's use.
    - A view that is useful to CSRs who want to look at an order and its shipment/tracking history
    - Simplest solution: create a view, and then just select data from it.
    > ```SQL
    > SELECT * FROM [Brazil Customers];
    > ```
- A stored procedure that can be called by a query to perform some math operation on the data and returns a value(s).
    - Get combined wages per job w/ a given job type, # hours
    - How many orders/shipments were carried on a vessel in a given amount of time
- A stored procedure that uses a cursor to access and manipulate (update/change) data.
    - Query to update rows that are under a particular wage, in order to comply with updated min. wage
    - Query to change the company owning a series of vessels, in case of buyout
    - Get vessels that are inactive, and randomly assign them to a shipment?
        - A shipment can be scheduled in the future and can exist in the `SHIPMENT` table w/ a null `vessel_id`, so randomly assign a vessel with no associated shipment to it
- A trigger that updates/inserts data based on an insert. 
    - Trigger that is used to randomly assign a customer service representative to a new service ticket
    - Trigger that updates the order_delivered_timestamp in the Order table when an order that has been delivered (indicated by the most recent waypoint id matching the order's address_id_destination), and puts the current DATETIME when running the trigger into order_delivered_timestamp for that order id
- A query that demos the trigger.
    - Simple insertion of open service ticket