import cmd
import location as iss
import globe as g

class Dashboard(cmd.Cmd):
    prompt = "iss_dash/> "

    def preloop(self):
        iss.create_timer()

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
    
    def do_fetch(self, line):
        """Get current location of ISS"""
        iss.save_location()

    def do_change_freq(self, line):
        """Change the automatic fetch frequency"""
        iss.cancel_timer()
        iss.set_frequency(float(line))
        iss.create_timer()

    def do_cancel(self, line):
        """Cancel the current timer"""
        iss.cancel_timer()

if __name__ == "__main__":
    Dashboard().cmdloop()