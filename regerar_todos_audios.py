import asyncio
import os
import edge_tts

# Dicionário completo de todos os áudios do Dojo Quest com grafia nativa japonesa
TODOS_AUDIOS = {
    # ==========================================
    # 1. CONTAGEM JAPONESA (1 A 20)
    # Padrão marcial estrito: Shi (4), Shichi (7), Ju-shi (14), Ju-shichi (17)
    # ==========================================
    "1": "いち",
    "2": "に",
    "3": "さん",
    "4": "し",
    "5": "ご",
    "6": "ろく",
    "7": "しち",
    "8": "はち",
    "9": "きゅう",
    "10": "じゅう",
    "11": "じゅういち",
    "12": "じゅうに",
    "13": "じゅうさん",
    "14": "じゅうし",
    "15": "じゅうご",
    "16": "じゅうろく",
    "17": "じゅうしち",
    "18": "じゅうはち",
    "19": "じゅうく",
    "20": "にじゅう",

    # ==========================================
    # 2. VOCABULÁRIO DO JUDÔ (23 TERMOS)
    # ==========================================
    "sensei": "先生",                     # せんせい
    "hajime": "はじめ",                   # Iniciar
    "mate": "待て",                       # まて
    "senpai": "先輩",                     # せんぱい
    "kohai": "後輩",                     # こうはい
    "uke": "受け",                       # うけ
    "tori": "取り",                       # とり
    "judogi": "柔道着",                   # じゅうどうぎ
    "wagui": "上衣",                     # うわぎ (wagui/uwagi tradicional)
    "shitabaki": "下穿き",                # したばき
    "obi": "帯",                         # おび
    "zori": "草履",                       # ぞうり
    "dojo": "道場",                       # どうじょう
    "randori": "乱取り",                  # らんどり
    "uchikomi": "打ち込み",               # うちこみ
    "soremade": "それまで",               # Fim do combate
    "ashi": "足",                         # あし
    "te": "手",                           # て
    "eri": "襟",                         # えり
    "sode": "袖",                         # そで
    "mokuso": "黙想",                     # もくそう
    "arigato": "ありがとうございます",     # Arigatô Gozaimasu formal completo
    "sayonara": "さようなら",              # さようなら

    # ==========================================
    # 3. PROJEÇÕES EM PÉ (TACHI-WAZA)
    # ==========================================
    "o-soto-gari": "オオソトガリ",          # 大外刈
    "de-ashi-barai": "デアシバライ",        # 出足払
    "o-uchi-gari": "オオウチガリ",          # 大内刈
    "ko-uchi-gari": "コウチガリ",          # 小内刈
    "o-soto-guruma": "オオソトグルマ",      # 大外車
    "o-goshi": "オオゴシ",                  # 大腰
    "harai-goshi": "ハライゴシ",            # 払腰
    "koshi-guruma": "コシグルマ",          # 腰車
    "ippon-seoi-nage": "イッポンセオイナゲ", # 一本背負投
    "tai-otoshi": "タイオトシ",            # 体落

    # ==========================================
    # 4. NE-WAZA (TÉCNICAS DE SOLO / IMOBILIZAÇÕES)
    # ==========================================
    "kesa-gatame": "ホンケサガタメ",        # 本袈裟固
    "yoko-shiho-gatame": "ヨコシホウガタメ", # 横四方固
    "kami-shiho-gatame": "カミシホウガタメ"  # 上四方固
}

VOZ = "ja-JP-NanamiNeural"
TAXA_VELOCIDADE = "-10%"  # Cadência nítida para crianças e estudantes

async def gerar_arquivo(chave, texto):
    caminho = os.path.join("audios", f"{chave}.mp3")
    comunicador = edge_tts.Communicate(texto, voice=VOZ, rate=TAXA_VELOCIDADE)
    await comunicador.save(caminho)
    print(f"✓ [{chave}.mp3] -> {texto}")

async def main():
    os.makedirs("audios", exist_ok=True)
    print(f"Iniciando a geração de {len(TODOS_AUDIOS)} áudios fonéticos...\n")
    for chave, texto in TODOS_AUDIOS.items():
        await gerar_arquivo(chave, texto)
    print("\nTodos os 46 áudios do Dojo Quest foram atualizados com perfeição fonética!")

if __name__ == "__main__":
    asyncio.run(main())
