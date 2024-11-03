In this project, I developed a framework to test a special HMI pretty simple and installed in many device. Lot of features, blanks, and options of this HMI are shared between all devices. 
So, to improve the quality and the efficience of the HMI production, I offered to create a framework test with selenium which allowed the developer to test new features added or modified 
in the HMI. 

There are three pages in this HMI: manager, alarms and expert. Each page with its own url. For each page I created a class with method for testing many things in each page.

For example, to test a neaw feature you have to instance an object of the page where the feature has been implemented. Then, you can call the different methods with the Xpath or the id 
of the element tested.

