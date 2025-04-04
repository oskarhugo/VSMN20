import numpy as np
import calfem.core as cfc
import calfem.utils as cfu
import tabulate as tab
import json

class ModelParams:
    """Class defining the parameters of the model."""
    def __init__(self):
        
            self.version=1
            self.t=1
            self.ep=[self.t]

            # --- Element properties ---
            self.k_x=50     # m/day
            self.k_y=50     # m/day
            self.D=np.array([
                    self.k_x, 0,
                    0, self.k_y
            ])
            self

            # --- Create input för the mesh ---
            self.coord=np.array([
                  [0.0, 0.0],
                  [0.0, 600.0],
                  [600.0, 0.0],
                  [600.0, 600.0],
                  [1200.0, 0.0],
                  [1200.0, 600.0]
            ])

            self.ex=np.array([
                  [0.0, 0.0, 600.0],
                  [0.0, 600.0, 600.0],
                  [600.0, 600.0, 1200.0],
                  [600.0, 1200.0, 1200.0]
            ])

            self.ey=np.array([
                  [0.0, 600.0, 600.0],
                  [0.0, 600.0, 0.0],
                  [0.0, 600.0, 600.0],
                  [0.0, 600.0, 0.0]
            ])
            # --- Element topology ---
            self.edof=np.array([
                  [1, 4, 2],
                  [1, 3, 4],
                  [3, 6, 4],
                  [3, 5, 6]    
            ])
            # --- Loads ---
            self.loads=[[
                  [6, -400]
            ]]

            # --- Boundary conditions ---
            self.bcs=[[
                 [1, 0.0],
                 [2, 60.0],
                 [3, 0.0],
                 [4, 60.0]
            ]]

            self.dof=None

def save(self,filename):
     """Save input to file."""
     model_params={}
     model_params["version"]=self.version
     model_params["t"]=self.t
     model_params["ep"]=self.ep
     model_params["coord"]=self.coord.tolist() # Convert NumPy array to list for JSON compatibility
     
     ofile=open(filename, "w")
     json.dump(model_params, ofile, sort_keys=True, indent=4)
     ofile.close()

def load(self, filename):
     """Load input from file."""
     ifile=open(filename, "r")
     model_params=json.load(ifile)
     ifile.close()

     self.version=model_params["version"]
     self.t=model_params["t"]
     self.ep=model_params["ep"]
     self.coord=np.array(model_params["coord"]) # Convert list back to NumPy array

class ModelResult:
      """Class for storing results from calculations."""
      def __init__(self):
            self.a=None
            self.r=None
            self.ed=None
            self.qs=None
            self.qt=None

class ModelSolver:
    """Class for perfoming the model computations."""
    def ___init__(self, model_params, model_result):
        self.model_params=model_params
        self.model_result=model_result

        def execute(self):
            # --- Assign shorter variable names from model properties
            edof=self.model_params.edof
            coord=self.model_params.coord
            dof=self.model_params.dof
            ep=self.model_params.ep
            loads=self.model_params.loads
            bcs=self.model_params.bcs
            D=self.model_params.D
            ex=self.model_params.ex
            ey=self.model_params.ey

            # --- Calculate stifnfness matrix and assemle global stiffness matrix ---
            K=np.zeros((6, 6))
            f=np.zeros((6, 1))
            f[5]=-400

            # --- Calculate element stiffness matrix and assemble global stiffness matrix ---
            ke1=cfc.flw2te(ex[0,:], ey[0,:], ep, D)
            ke2=cfc.flw2te(ex[1,:], ey[1,:], ep, D)
            ke3=cfc.flw2te(ex[2,:], ey[2,:], ep, D)
            ke4=cfc.flw2te(ex[3,:], ey[3,:], ep, D)

            # --- Assemble global stiffness matrix ---
            K=cfc.assem(edof[0,:], ke1, K)
            K=cfc.assem(edof[1,:], ke2, K)
            K=cfc.assem(edof[2,:], ke3, K)
            K=cfc.assem(edof[3,:], ke4, K)

            # --- Calculate flow ---
            
            for load in loads:
                 dof=load[0]
                 mag=load[1]
                 f[dof-1]=mag

            bc_prescr=[]
            bc_value=[]

            for bc in bcs:
                 dof=bc[0]
                 value=bc[1]
                 bc_prescr.append(dof)
                 bc_value.append(value)

            
            bc_prescr=np.array(bc_prescr)
            bc_value=np.array(bc_value)

            a, r=cfc.flw2solve(K, f, bc_prescr, bc_value)

            # --- Calculate element flows and gradients ---
            n_el=edof.shape[0]
            es=np.zeros([n_el, 2])
            et=np.zeros([n_el, 2])
            ed=cfc.extractEldisp(edof, a)

            for elx, ely, eld, eles, elet in zip(ex, ey, ed, es, et):
                 es_el,et_el=cfc.flw2ts(elx, ely, D, eld)
                 eles[:]=es_el[0,:]
                 elet[:]=et_el[0,:]
            
class ModelReport:
     """Class for presenting input and output parameters in report form."""
     def __init__(self, model_params, model_result):
            self.model_params=model_params
            self.model_result=model_result
            self.report=""

     def clear(self):
          self.report=""
     
     def add_text(self, text=""):
          self.report+=str(text)+"\n"

     def __str__(self):
          self.clear()
          self.add_text()
          self.add_text("-------------- Model input ----------------------------------")
          # ...
          self.add_text("Coordinates")
          self.add_text()
          self.add_text(
               tab.tabulate(self.params.edof, headers=["x", "y"], tablefmt="psql")
          )

          return self.report



            





