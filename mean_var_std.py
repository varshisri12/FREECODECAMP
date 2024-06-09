import numpy as np

def calculate(array):
  if (len(array)<9):
    # print("lenght = ",len(array))
    return ("List must contain nine numbers.")
  else:
    array_input = [array[0:3],array[3:6], array[6:9]]

    mean_axis1 = [0,0,0]
    mean_axis2 = [0,0,0]
    var_axis1 = [0,0,0]
    var_axis2 = [0,0,0]
    std_axis1 = [0,0,0]
    std_axis2 = [0,0,0]

    for i in range (3):
      mean_axis1[i] = np.mean([array_input[0][i],array_input[1][i],array_input[2][i]])
      mean_axis2[i] = np.mean(array_input[i])

      var_axis1[i] = np.var([array_input[0][i],array_input[1][i],array_input[2][i]])
      var_axis2[i] = np.var(array_input[i])

      std_axis1[i] = np.std([array_input[0][i],array_input[1][i],array_input[2][i]])
      std_axis2[i] = np.std(array_input[i])


    mean = [mean_axis1, mean_axis2, np.mean(array)]
    var = [var_axis1, var_axis2, np.var(array)]
    std = [std_axis1, std_axis2, np.std(array)]

    return {'mean':mean, 'variance':var, 'standard deviation':std}