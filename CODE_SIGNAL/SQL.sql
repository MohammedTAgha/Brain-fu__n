FROM     expressions
WHERE    c = IF( operation = '+', a+b,
             IF( operation = '-', a-b,
             IF( operation = '*', a*b,
             IF( operation = '/', a/b, NULL ))))
             
              SELECT *
    FROM expressions
    WHERE calc(a,b,operation) = c
    ORDER BY id;    
END;

CREATE FUNCTION calc ( a DOUBLE, b DOUBLE, op varchar(1) ) RETURNS DOUBLE
BEGIN
    CASE op
        WHEN "+" THEN SET @calc = a+b;
        WHEN "-" THEN SET @calc = a-b;
        WHEN "*" THEN SET @calc = a*b;
        WHEN "/" THEN SET @calc = a/b;
    END CASE;
   RETURN @calc;
   
    SELECT * FROM expressions
        WHERE (operation = '+' AND a + b = c) OR 
              (operation = '-' AND a - b = c) OR 
              (operation = '*' AND a * b = c) OR
              (operation = '/' AND b != 0 AND C * b = a);
              *******
              
  SELECT * FROM expressions
    WHERE CASE operation
        WHEN '+' THEN a + b
        WHEN '-' THEN a - b
        WHEN '*' THEN a * b
        WHEN '/' THEN a / b
      END = c
    ORDER BY id;
    ----------------------------
    select * 
        from expressions
        where elt(locate(operation, "+-*/"), a+b, a-b, a*b, a/b) = c;
        
        ----------------------
        /*Please add ; after each select statement*/
CREATE PROCEDURE solution()
BEGIN
    SELECT *
    FROM expressions
    WHERE calc(a,b,operation) = c
    ORDER BY id;    
END;

CREATE FUNCTION calc ( a DOUBLE, b DOUBLE, op varchar(1) ) RETURNS DOUBLE
BEGIN
    CASE op
        WHEN "+" THEN SET @calc = a+b;
        WHEN "-" THEN SET @calc = a-b;
        WHEN "*" THEN SET @calc = a*b;
        WHEN "/" THEN SET @calc = a/b;
    END CASE;
   RETURN @calc;
END;
----
