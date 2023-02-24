'''
- Data Pre-Processing for Decision Tree -
-> Copyright © 2023 Emre MENTEŞE. All rights reserved.
'''

import matplotlib.pyplot as plt
import matplotlib as mpl

class Data:
    xlim = [-1.5, 1.5]
    ylim = [-1.5, 1.5]
    train_instances = []
    test_instances = []

    def __init__(self, features,Type):
        if (isinstance(features, dict)):
            self.features = features
            self.type = str(Type)

            if str(Type) == "train":
                self.__class__.train_instances.append(self)
            elif str(Type) == "test":
                self.__class__.test_instances.append(self)
            else:
                raise Exception("Undefined data Type value")
        else:
            raise Exception("Type error for data.")
        
    def __str__(self) -> str:
        keys = list(self.features.keys())
        return f"{self.features[keys[0]]} -   {self.features[keys[1]]}  -   {self.features[keys[2]]}"
    
    def view_item(self):
        try:
            keys = list(self.features.keys())
            plt.figure("Item Review")
            plt.title(self.__str__())
            plt.scatter(self.features[keys[0]],self.features[keys[1]], color="black", s=5)
            plt.xlabel('X Value')
            plt.ylabel('Y Value')
            plt.xlim(self.xlim)
            plt.ylim(self.ylim)
            plt.colorbar()
            plt.show()

        except Exception as e:
            raise Exception(f"Data review error: {e}")
        else:
            return True

    @classmethod
    def view_data(self,Type):
        if str(Type) == "train":
            all_data = Data.train_instances
        elif str(Type) == "test":
            all_data = Data.test_instances
        else:
            raise Exception("Undefined data Type value")

        plt.figure("Data Review")
        plt.title("Data Review")
        
        x_axis = []
        y_axis = []
        c_axis = []
        for d in all_data:
            keys = list(d.features.keys())
            x_axis.append(d.features[keys[0]])
            
            y_axis.append(d.features[keys[1]])
            
            c_axis.append(d.features[keys[2]])

        cm = mpl.colors.LinearSegmentedColormap.from_list(name="Gruplar", colors=["black", "green", "#808000", "red"], N=4)

        plt.scatter(x_axis, y_axis, c=c_axis, cmap=cm, s=5)
        plt.xlabel('X Value')
        plt.ylabel('Y Value')
        plt.xlim(self.xlim)
        plt.ylim(self.ylim)
        plt.clim(-0.5, 3.5)
        cb = plt.colorbar(ticks=range(0, 4), label='Group', orientation="horizontal")
        cb.ax.tick_params(length=0)
        cb.set_ticklabels(["Test", "Yeşil", "Sarı", "Kırmızı"])
        plt.show(block = True)
        return True

# read train data
def rtraind():
    data = []
    try:

        #open the file test or train data file
        with open("src/train.txt", "r", encoding="utf-8") as file:
            read_data = file.readlines()
            for n in read_data:
                lastdata = []
                data2 = n.replace("\n", " ").replace("\t", " ").split(" ")

                # control data type
                for i in data2:
                    try:
                        lastdata.append(float(i))
                    except:
                        continue

                data_dict = {"X": lastdata[0],"Y": lastdata[1], "Color": lastdata[2]}
                new = Data(data_dict,"train")
                data.append(new)

            return data

    except Exception as e:
        print(f"Data read error: {e}")

# read test data
def rtestd():
    data = []
    try:

        #open the file test or train data file
        with open("src/test.txt", "r", encoding="utf-8") as file:
            read_data = file.readlines()
            for n in read_data:
                lastdata = []
                data2 = n.replace("\n", " ").replace("\t", " ").split(" ")

                # control data type
                for i in data2:
                    try:
                        lastdata.append(float(i))
                    except:
                        continue

                data_dict = {"X": lastdata[0],"Y": lastdata[1], "Color": lastdata[2]}
                new = Data(data_dict, "test")
                data.append(new)

            return data

    except Exception as e:
        print(f"Data read error: {e}")
