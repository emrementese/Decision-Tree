# Decision-Tree
Basic Decision Tree with python

Hi everyone !
  
  My name is Emre MENTEŞE and I study Electric - Electronic Engineering at Istanbul Medeniyet University. I would like to share my computer programming project for you. This project was created and given by Dr. Caner Sahin. The project about basic decision tree. Versions of the project designed for C or C++ programming language with dynamic memory but I arranged again for python with multithreading programming. I uploaded a PDF file for decision tree project but this PDF file's language is Turkish. That's why I will explain the project file a little.
  
For you can understand this project, you must know the some python subjects;
--> Basic python information.
--> File operation for python.
--> Object oriented programming for python.
--> Multithreading programming for python.
--> And some python modules.

  Firstly we will train the decision tree with first data. After that we'll test the decision tree with second data. The data has got 3 criterias. We know 2 criterias and we'll guess last criterion. Every data can like an apple for a more concrete statement. Think apples. Apples on the table. Table has got a coordinate system as x-y as. Center of the table is origin for coordinate system. We have thought every data-apple has got 3 criterias. First criterion is apple's x coordinate. Second criterion is apple's y coordinate. Third criterion is apple's color.
  
  We have thought, we have got 2 datas. First Data and Second Data. First data file is train.txt and we use this file for train the decision tree. You can see in the file, the file has got 150 rows and 3 columns. First column is apple's x coordinate. Second column is apple's y coordinate. Third column is apple's color. So, we have got 150 apples and every apple has got 3 criterias. If you look at the train.txt file , you can see integers ( 1 - 2 - 3 ) for third column. If third column's data == 1 --> This apple color is "YELLOW". Elif third column's data == 2 --> This apple color is "RED" Elif third column's data == 3 --> This apple color is "Green".
  
  For apples has got, only 1 color (Yellow - Red - Green), only 1 x coordinate, only  1 y coordinate. If you look at the test.txt file (We use this file for test decision tree), you can see "0" for third column. That's mean we don't know apple color's. This is the purpose. Guess. When test.txt is exported to the decision tree, decision tree'll say the apple's color for we. This is the logic of the decision tree. Guess a criterion of new data using old data.
  
  So, When coding a decision tree, you must follow certain rules. This rules is; Iteration , Entropy , Termination criterias ,nodes (root- child or normal - leaf).
  
  
 
