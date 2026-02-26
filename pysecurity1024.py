# pysecurity1024.py

import secrets
import string
import math

# Constantes expostas para o pacote
ALFABETO = string.ascii_letters
DIGITOS = string.digits

class SecurityEngine:
    """Motor de segurança para geração de entropia em sistemas neurais."""
    
    def __init__(self, num_blocos=27, letras_fixas=10):
        self.num_blocos = num_blocos
        self.letras_fixas = letras_fixas
        self.alfabeto = ALFABETO
        self.digitos = DIGITOS

    def calcular_bits(self, tamanho, base_len):
        """Calcula a entropia: H = L * log2(N)"""
        return tamanho * math.log2(base_len)

    def gerar_letras(self, qtd):
        """Gera uma sequência aleatória de letras."""
        return ''.join(secrets.choice(self.alfabeto) for _ in range(qtd))

    def gerar_palavra(self, min_len=6, max_len=7):
        """Gera uma palavra dinâmica + 1 dígito."""
        tamanho = secrets.randbelow(max_len - min_len + 1) + min_len
        letras = ''.join(secrets.choice(self.alfabeto) for _ in range(tamanho))
        digito = secrets.choice(self.digitos)
        
        bits = self.calcular_bits(tamanho, len(self.alfabeto)) + self.calcular_bits(1, len(self.digitos))
        return f"{letras}{digito}", bits

    def gerar_id_aleatorio(self, min_len=7, max_len=10):
        """Gera IDs únicos para neurônios da Suprema."""
        tamanho = secrets.randbelow(max_len - min_len + 1) + min_len
        return ''.join(secrets.choice(self.alfabeto) for _ in range(tamanho))

    def gerar_frase_mestra(self):
        """Gera a 'Seed' de alta segurança para a Inteligência Suprema."""
        inicio = self.gerar_letras(self.letras_fixas)
        fim = self.gerar_letras(self.letras_fixas)
        
        meio_lista = []
        entropia_total = self.calcular_bits(self.letras_fixas * 2, len(self.alfabeto))

        for _ in range(self.num_blocos):
            p, b = self.gerar_palavra()
            meio_lista.append(p)
            entropia_total += b

        frase = f"{inicio}{''.join(meio_lista)}{fim}"
        return {
            "token": frase,
            "entropia_bits": round(entropia_total, 2),
            "seguranca": "Suprema" if entropia_total > 1024 else "Alta"
        }

if __name__ == "__main__":
    engine = SecurityEngine()
    resultado = engine.gerar_frase_mestra()
    print(f"\n--- Motor de Segurança Ativado ---")
    print(f"Token (truncado): {resultado['token'][:30]}...")
    print(f"Força de Entropia: {resultado['entropia_bits']} bits")
    print(f"Nível de Segurança: {resultado['seguranca']}")
