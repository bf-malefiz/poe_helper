import Gui, sys
    
def main():
    app = Gui.QApplication(sys.argv)
    ex = Gui.App()
    ex.show()

    sys.exit(app.exec_())
	
if __name__ == '__main__':
    main()