import asyncio
import os
import edge_tts

# Dicionário mapeando a chave do arquivo .mp3 para a escrita fonética pura em japonês
GOLPES_FONETICOS = {
    # Módulo 8: Projeções em Pé (Tachi-waza)
    "o-soto-gari": "オオソトガリ",          # 大外刈 (sem pausas no 'o' ou som aportuguesado)
    "de-ashi-barai": "デアシバライ",        # 出足払 (pronúncia fluida contínua)
    "o-uchi-gari": "オオウチガリ",          # 大内刈
    "ko-uchi-gari": "コウチガリ",          # 小内刈
    "o-soto-guruma": "オオソトグルマ",      # 大外車
    "o-goshi": "オオゴシ",                  # 大腰
    "harai-goshi": "ハライゴシ",            # 払腰
    "koshi-guruma": "コシグルマ",          # 腰車
    "ippon-seoi-nage": "イッポンセオイナゲ", # 一本背負投
    "tai-otoshi": "タイオトシ",            # 体落

    # Módulo 9: Ne-Waza (Imobilizações)
    "kesa-gatame": "ホンケサガタメ",        # 本袈裟固
    "yoko-shiho-gatame": "ヨコシホウガタメ", # 四方固 com o 'o' longo natural (ほう)
    "kami-shiho-gatame": "カミシホウガタメ"  # 上四方固
}

VOZ = "ja-JP-NanamiNeural"
TAXA_VELOCIDADE = "-10%"  # Leve desaceleração para clareza didática sem quebrar o tom

async def gerar_audio(chave, texto_katakana):
    caminho_arquivo = os.path.join("audios", f"{chave}.mp3")
    print(f"Gerando áudio para '{chave}' -> {texto_katakana}...")
    comunicador = edge_tts.Communicate(texto_katakana, voice=VOZ, rate=TAXA_VELOCIDADE)
    await comunicador.save(caminho_arquivo)

async def main():
    os.makedirs("audios", exist_ok=True)
    for chave, texto in GOLPES_FONETICOS.items():
        await gerar_audio(chave, texto)
    print("\nTodos os áudios de golpes e técnicas foram regerados com sucesso!")

if __name__ == "__main__":
    asyncio.run(main())
