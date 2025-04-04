import gwflow as fm

if __name__ == "__main__":
    model_params=fm.ModelParams()
    model_result=fm.ModelResult()
    
    solver=fm.ModelSolver(model_params, model_result)
    solver.execute()

    report=fm.ModelReport(model_params, model_result)
    print(report)