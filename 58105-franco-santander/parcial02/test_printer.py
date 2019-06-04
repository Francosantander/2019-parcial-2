import unittest
from printer import Printer

class TestImpresora(unittest.TestCase):
    def test_setUp(self):
        self.impresora = Printer()
    
    def test_nada_imprimir(self):
        impresora = Printer()
        self.assertFalse(impresora.printing)
        self.assertFalse(impresora.error_flag)
        self.assertEqual(impresora.error_description,'')
        #Nada imprimendo
        self.assertTrue(impresora.printer_available())
        #Nada en la cola
        self.assertEqual(impresora.queue_printer,[])

    def test_imprimir_ok(self):
        impresora = Printer()
        impresora.add_print_job('HOLA MUNDO')
        impresora.print_job()
        #CUANDO ESTA IMPRIENDO
        self.assertFalse(impresora.printer_available())
        self.assertFalse(impresora.error_flag)
        self.assertEqual(impresora.queue_printer,[])
        #Cuando termina de imprimir, reseteamos la impresora
        impresora.reset_printer()
        #Cambia el estado de la impresora
        self.assertTrue(impresora.printer_available())
        self.assertFalse(impresora.error_flag)
    
    def test_impresion_nada_para_imprimir(self):
        impresora = Printer()
        impresora.print_job()
        #Error ya que no hay nada para imprimir
        self.assertTrue(impresora.error_flag)
        self.assertEqual(impresora.error_description,'nothing to print')
        #Despues del error, se resetea la impresora
        impresora.reset_printer()
        self.assertFalse(impresora.printing)
        self.assertFalse(impresora.error_flag)




    

if __name__ == "__main__":

   unittest.main()