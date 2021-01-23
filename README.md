# bell-nozzle-contour

@ THIS PROJECT AIM IS TO GENERATE BELL NOZZLE CONTOUR IN YOUR RESPECTIVE DESIGNING SOFTWARE'S (LIKE-> CATIA, ANSYS, etc.) @

===> THIS CODE ONLY WORKS ON "PYTHON" LATEST VERSIONS  <===

=> LINK TO DOWNLOAD "PYTHON" : https://www.python.org/downloads/

==>BEFORE USING THIS CODE PLEASE DOWNLOAD THE 2 EXCEL FILES

   1) 'NOZZLEPARA' CONSISTS OF FEW NOZZLE PARAMETERS, MAKE RESPECTIVE CHANGES IN IT TO GET YOUR DESIRED NOZZLE CONTOUR.

      --> AFTER DOWNLOADING THE EXCEL SHEET IN YOUR SYSTEM, COPY THE FILE PATH AND 
          REPLACE IT WITH THE PATH ALREADY PRESENT INSIDE THE CODE(INSIDE READ EXCEL FUNCTION).
      
      --> df = read_excel(r' ENTER YOUR FILE PATH HERE!! ')
    
   2) 'NOZZLEPTS' FILE CONTAINS ALL THE COORDINATES GENERATED FROM THE CODE.
    
      --> BASICALLY AFTER YOU RUN THE CODE, THE COORDINATES GENERATED FROM 
          THE CODE WILL BE STORED IN YOUR DESIRED EXCEL SHEET.
      
      --> TO STORE IN YOUR DESIRED EXCEL SHEET JUST REPLACE THE FILE NAME 'nozzlepts.xls'
          WITH YOUR DESIRED ONE NEAR THE LAST LINE OF CODE (ex: wb.save('example.xls') ).
          
==> DEMO VALUES ARE GIVEN IN THE EXCEL SHEETS (TAKEN FROM "VDEngineering") 
    AND ALSO THE PLOTS OBTAINED FROM THE VALUES ARE AVAILABLE FOR REFERENCE.
    
*NOTE:

 => BEFORE YOU RUN THE CODE MAKE SURE THAT THE FOLLOWING PYTHON PACKAGES ARE INSTALLED :
  
   1)PANDAS      (LINK : https://pypi.org/project/pandas/#files )
  
   2)SCIPY       (LINK : https://pypi.org/project/scipy/#files )
 
   3)MATPLOTLIB  (LINK : https://pypi.org/project/matplotlib/#files )
  
   4)XLWT        (LINK : https://pypi.org/project/xlwt/#files )

=> AFTER DOWNLOADING THE RESPECTIVE PACKAGES OPEN COMMAND PROMPT IN YOUR SYSTEM.

=> AFTER OPENING COMMAND PROMPT TYPE " pip install 'package name' ", DO THIS FOR ALL THE DOWNLOADED PACKAGES.

=> EXAMPLE : " pip install pandas " (excluding double quotes).

<meta name="google-site-verification" content="KC-jkfMcZ1gkI8SeSYmTmi0MqmNktMEDxA7YtV2D_pY" />
