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
        
        savetxt(layer_path+"Wi.csv",W[:,:units],delimiter=',')
        savetxt(layer_path+"Wf.csv",W[:,units:units*2],delimiter=',')
        savetxt(layer_path+"Wc.csv",W[:,units*2:units*3],delimiter=',')
        savetxt(layer_path+"Wo.csv",W[:,units*3:],delimiter=',')
        savetxt(layer_path+"Ui.csv",U[:,:units],delimiter=',')
        savetxt(layer_path+"Uf.csv",U[:,units:units*2],delimiter=',')
        savetxt(layer_path+"Uc.csv",U[:,units*2:units*3],delimiter=',')
        savetxt(layer_path+"Uo.csv",U[:,units*3:],delimiter=',')
        savetxt(layer_path+"bi.csv",b[:units],delimiter=',')
        savetxt(layer_path+"bf.csv",b[units:units*2],delimiter=',')
        savetxt(layer_path+"bc.csv",b[units*2:units*3],delimiter=',')
        savetxt(layer_path+"bo.csv",b[units*3:],delimiter=',')
    
    #save dense top layer
    dense_top = model.layers[-1]
    in_weights, out_weights = dense_top.get_weights()
    layer_path = savpath + "./dense_top./"
    if(not path.exists(layer_path)):
        os.mkdir(layer_path)    
    savetxt(layer_path+"in_weights.csv",in_weights,delimiter=',')
    savetxt(layer_path+"out_weights.csv",out_weights,delimiter=',')