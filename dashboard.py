import cmd
import location as iss
import globe as g

class Dashboard(cmd.Cmd):
    prompt = "iss_dash/> "

    def preloop(self):
        iss.save_location()

    def postloop(self):
        iss.insert_breakpoint()

    def do_set_breakpoint(self, line):
        """Create a breakpoint"""
        iss.insert_breakpoint()
    
    def do_exit(self, line):
        """Stop the tracker"""
        iss.cancel_timer()
        return True
    
    def do_view(self, line):
        """Start up the GUI"""
        fig = g.create_globe_plot()
        fig.show()

if __name__ == "__main__":
    Dashboard().cmdloop()