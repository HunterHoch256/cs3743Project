delimiter //
CREATE PROCEDURE fillwaypoints ()
BEGIN
	DECLARE cur_w int unsigned DEFAULT 0;
    
    upd: LOOP
		SET cur_w = cur_w + 1;
		-- If we haven't reached the last waypoint address ID then
        IF cur_w < 255 THEN
			INSERT INTO WAYPOINT (address_id)
			VALUES (cur_w);
            
            ITERATE upd;
		END IF;
        -- Else
        LEAVE upd;
        
	END LOOP upd;
END//
delimiter ;
-- Time to test!
START TRANSACTION;

CALL fillwaypoints();

-- Verify
SELECT *
FROM WAYPOINT;
-- Verify w/ join
SELECT waypoint_id, address_line1, address_city, address_state
FROM WAYPOINT JOIN ADDRESS USING (address_id);

-- It worked!
COMMIT;