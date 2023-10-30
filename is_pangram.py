def is_pangram(s):
    """
    Verifica se a string dada é um pangrama, ou seja, se contém todas as letras do alfabeto latino pelo menos uma vez.

    Args:
        s (str): A string a ser verificada.

    Returns:
        bool: True se a string é um pangrama, False caso contrário.
    
    Nota importante:
    Esta solução não trata caracteres especiais da tabela Unicode/ASCII na versão 1.0.
    
    Para mais informações, consulte: https://www.codewars.com/kata/545cedaa9943f7fe7b000048/train/python
    """
    # Lista com todas as letras do alfabeto latino
    alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    
    # Cria uma lista vazia para coletar as letras do alfabeto presentes na string
    letras_unicas = []
    
    # Percorre a string em minúsculas
    for c in s.lower():
        # Verifica se cada caractere "c" está no alfabeto
        if c in alfabeto:
            letras_unicas.append(c)  # Adiciona o caractere "c" à lista de letras únicas
    
    # Remove duplicatas da lista de letras únicas
    for c in letras_unicas:
        while letras_unicas.count(c) > 1:
            letras_unicas.remove(c)
    
    # Ordena a lista de letras únicas e compara se é igual à lista do alfabeto
    return sorted(letras_unicas) == alfabeto

# Exemplos
print(is_pangram("The quick, brown fox jumps over the lazy dog!"))  # Deve retornar True
print(is_pangram("1bcdefghijklmnopqrstuvwxyz"))  # Deve retornar False
print(is_pangram("The quick brown fox jumps over the lazy dog."))  # Deve retornar True
print(is_pangram("ABCD45EFGH,IJK,LMNOPQR56STUVW3XYZ"))  # Deve retornar True
