# HSBC RAP - Recepción Automatizada de Pagos
_La Recepción Automatizada de Pagos (RAP) proporciona una solución eficiente para identificar los depósitos de su cobranza_
## Módulo de validación 10
_Este módulo de validación, calcula el dígito verificador únicamente de la referencia que proporciona el cliente, la
referencia puede ser numérica o alfanumérica y con una longitud máxima de 39 caracteres_
### Digito verificador
_Referencia del cliente 19928756_
_Llamada a la función modulo10, para obtener la referencia de pago_
``
referencia = modulo10('19928756')
print("Referencia: " + referencia) # 199287566
``
### HSBC adicional
_Para mayor información contactar a los ejecutivos de HSBC_
