# LabVIEW-LSTM
LabVIEW library for deploying LSTMS in LabVIEW and LabVIEW Real-Time. This library lets the user upload weights to create custom LSTM cell VIs that can easily be deployed onto LabVIEW or LabVIEW Real-Time. 

<p align="center">
<img src="figures/single-LSTM-cell-use.PNG" alt="drawing" width="400"/> <br> 

</p>
<p align="center">
</p>
Each LSTM VI stores its weights and performs calculations to update cell state. Time steps are implemented with shift registers within a loop.

<p align="center">
<img src="figures/multiple-LSTM-cell-use.PNG" alt="drawing" width="400"/> <br> 

</p>
<p align="center">
</p>
Stacked LSTM sequences can be implemented by feeding the output of each LSTM layer to be the input of the next.

### How to create LSTM cell VIs
After installing the package a new palette should appear in the LabVIEW functions panel. Select "fill-lstm-template" or "fill-dense-template" depending on if you wish to make an LSTM cell or dense cell. Drag the VI to the workspace and double-click it to open the VI. Enter the name of the new cell and weight path into the appropriate fields. Run the VI and when the generated VI opens, "save as" to set the file location.
<p align="center">
<img src="figures/palette.PNG" alt="drawing" width="400"/> <br>
</p>

### Formatting .csv files
The matrices of weights for a cell should be stored in separate csv files withn a folder. Each file is named in the format "matrix" + "gate" + ".csv". Matrices are "W" (kernel), "U" (recurrent kernel), and "b" (bias). Gates are "i", "f", "c", and "o". Therefore names are Wi.csv, Uo.csv, bf.csv, etc. The python function given in ``create_weight_folder.py`` converts the weights of a keras LSTM model to this format.

### Represenitive Project and Publication
Daniel Coble, Joud Satme, Ehsan Kabir, Austin R.J. Downey, Jason D. Bakos, David Andrews, Miaoqing Huang, Adrine Moura, and Jacob Dodson. Towards online structural state-estimation with sub-millisecond latency. 92nd Shock and Vibration Symposium, September 2022. [PDF](https://cse.sc.edu/~adowney2/publications/conference/Coble2022TowardsOnlineStructural.pdf), [repo](https://github.com/ARTS-Laboratory/Paper-Towards-online-structural-state-estimation-with-sub-millisecond-latency)
 


## [Development Workspace](development_workspace)
Houses all the code used in building and developing the functions. 

## [Package](package)
Houses the published packages. See the latest package in "Releases".

## Licence and Citation
[![CC BY-SA 4.0][cc-by-sa-shield]][cc-by-sa]

This work is licensed under a
[Creative Commons Attribution-ShareAlike 4.0 International License][cc-by-sa].



[cc-by-sa]: http://creativecommons.org/licenses/by-sa/4.0/
[cc-by-sa-image]: https://licensebuttons.net/l/by-sa/4.0/88x31.png
[cc-by-sa-shield]: https://img.shields.io/badge/License-CC%20BY--SA%204.0-lightgrey.svg


Cite as:

Daniel Coble and Austin Downey. LabVIEW-LSTM. GitHub, 2022. [Online]. Available: https://github.com/ARTS-Laboratory/LabVIEW-LSTM

@Misc{Coble2022LabVIEWLSTM,  
author = {Daniel Coble and Austin Downey},  
howpublished = {GitHub},  
title = {{LabVIEW-LSTM}},  
year = {2022},  
groups = {{ARTS-L}ab},  
url = {https://github.com/ARTS-Laboratory/LabVIEW-LSTM},  
}

## Frequently Asked Questions (FAQ) for the LSTM LabVIEW Model

#### 1. What does this library do?
The package allows for pre-trained LSTM models to be deployed to a LabVIEW environment for inference. A VI is created to compute one timestep of an LSTM network. This allows inputs to be processed, and outputs created in a real-time framework where data can be accessed after every timestep.

#### 2. How do I input my data into the LSTM model?
Data is processed per timestep (not all at once). Within a loop, extract the input data and transform it into a vector that can be processed by the LSTM VI. If data is given in an Excel or CSV file, you can use a for-loop to iterate through the rows of data.

#### 3. What does the output of the LSTM model look like?
At each timestep, the output is a vector of values bounded between 0 and 1. The library also contains an implementation of a dense layer, which is commonly used to aggegate an LSTM output to a single value. Depending on your application, you can transform this vector into a double or an array of doubles for further analysis or decision-making.

#### 4. How are the weights of the LSTM cell generated?
For models trained with the Python `keras` library, a function is provided which takes a model and creates a properly formatted folder of `.csv` files containing model weights. The folder of weights is then used by the `fill-lstm-template` VI in LabVIEW to create the LSTM cell with the appropriate weight matrices.

#### 5. Can I use weights from a source other than Keras?
Weights from other sources need to be formatted properly to be understood by the `fill-lstm-template` VI. The current implementation supports weights generated from Keras, but if you're using a different source, you will need to ensure the weights are in `.csv` format and compatible with the LabVIEW VI.

#### 6. What should I do if I need help understanding the LSTM LabVIEW model?
You can refer to the most recent paper on this topic:  
[PDF: Towards Online Structural State Estimation with Sub-Millisecond Latency](https://cse.sc.edu/~adowney2/publications/conference/Coble2022TowardsOnlineStructural.pdf)  
[GitHub: ARTS-Laboratory LSTM Model](https://github.com/ARTS-Laboratory/Paper-Towards-online-structural-state-estimation-with-sub-millisecond-latency)

These resources provide examples of how the model has been used and may offer insight into applying it to your own data.
