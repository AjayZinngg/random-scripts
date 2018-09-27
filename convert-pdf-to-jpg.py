for (dirname, dirs, files) in os.walk('../'):
   for filename in files:
    print(dirname )
    if  filename.endswith('.pdf') :
        filename_new =filename.split('.')[0]
        command =  "convert -density 150 " +dirname + "/"+filename + " -quality 90 " +dirname + "/"+ filename_new + ".jpg"
        
        try:
            os.system(command)

        except Exception as e:
            raise e
            
       
