# save model weights as folder of csvs.
def save_model_weights_as_csv(model, savpath = "./model_weights"):
    import os
    import os.path as path
    from numpy import savetxt
    if(not path.exists(savpath)):
        os.mkdir(savpath)
    for layer in model.layers[:-1]: # the final layer is a dense top
        layer_path = savpath + "./" + layer.name + "./"
        if(not path.exists(layer_path)):
            os.mkdir(layer_path)
        W, U, b = layer.get_weights()
        units = U.shape[0]
        
        savetxt(layer_path+"Wi.csv",W[:,:units].T,delimiter=',')
        savetxt(layer_path+"Wf.csv",W[:,units:units*2].T,delimiter=',')
        savetxt(layer_path+"Wc.csv",W[:,units*2:units*3].T,delimiter=',')
        savetxt(layer_path+"Wo.csv",W[:,units*3:].T,delimiter=',')
        savetxt(layer_path+"Ui.csv",U[:,:units].T,delimiter=',')
        savetxt(layer_path+"Uf.csv",U[:,units:units*2].T,delimiter=',')
        savetxt(layer_path+"Uc.csv",U[:,units*2:units*3].T,delimiter=',')
        savetxt(layer_path+"Uo.csv",U[:,units*3:].T,delimiter=',')
        savetxt(layer_path+"bi.csv",b[:units],delimiter=',')
        savetxt(layer_path+"bf.csv",b[units:units*2],delimiter=',')
        savetxt(layer_path+"bc.csv",b[units*2:units*3],delimiter=',')
        savetxt(layer_path+"bo.csv",b[units*3:],delimiter=',')
    
    #save dense top layer
    dense_top = model.layers[-1]
    dense_weights = dense_top.get_weights()
    if(len(dense_weights) == 1): # no bias
        dense_weights = dense_weights[0]
        dense_bias = np.array([0])
    else:
        dense_weights, dense_bias = dense_weights
    layer_path = savpath + "./dense_top./"
    if(not path.exists(layer_path)):
        os.mkdir(layer_path)    
    savetxt(layer_path+"weights.csv",in_weights,delimiter=',')
    savetxt(layer_path+"bias.csv",out_weights,delimiter=',')

if __name__ == "__main__":
    import tensorflow.keras as keras
    model_filename = "./model_saves/modelname" # put saved model location here
    out_filename = "./model_weights/weightloc" # where you want the weights saved
    
    model = keras.models.load_model(model_filename)
    save_model_weights_as_csv(model, savpath=out_filename)
    
