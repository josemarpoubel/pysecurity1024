# test_generate_phrases.py

from pysecurity1024 import SecurityEngine

def gerar_amostras_registro(quantidade=7):
    engine = SecurityEngine()
    
    print(f"{'#'*80}")
    print(f"{'REGISTRO DE ENTROPIA COMPLETO - INFRAESTRUTURA SUPREMA':^80}")
    print(f"{'#'*80}\n")
    
    # Cabeçalho da tabela
    tabela_readme = "| ID | Token de Segurança Completo (Integridade Total) | Entropia (Bits) | Status |\n"
    tabela_readme += "|:---|:---|:---|:---|\n"

    for i in range(1, quantidade + 1):
        resultado = engine.gerar_frase_mestra()
        token = resultado['token']
        bits = resultado['entropia_bits']
        status = "SUPREMA"
        
        # Agora usando o token INTEIRO envolto em crases para o Markdown
        tabela_readme += f"| {i:02d} | `{token}` | {bits} | {status} |\n"
    
    # Exibe no terminal (pode quebrar a linha no console, mas no README fica reto)
    print(tabela_readme)
    
    # Salva no arquivo para você copiar direto para o README.md
    with open("amostras_readme.txt", "w") as f:
        f.write(tabela_readme)
    
    print(f"\n{'#'*80}")
    print(f" Registro Completo salvo em: 'amostras_readme.txt' ")
    print(f"{'#'*80}")

if __name__ == "__main__":
    gerar_amostras_registro()
