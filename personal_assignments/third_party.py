import matplotlib.pyplot as plt
import io
import urllib, base64

plt.switch_backend('AGG')  # Matplotlib'i AGG backend'e geçirin



def third_party_usage(positive, negative, notr):
        datas = [positive, negative, notr]

        if positive == 0 and negative == 0 and notr == 0:
            datas = [0,0,1]

        fig, ax = plt.subplots()
        wedges, texts, autotexts = ax.pie(datas, autopct='%0.5f%%')
        ax.axis('equal')
        
        # Add legend
        ax.legend(wedges, ["Pozitif Yorumlar", "Negatif Yorumlar", "Diğerleri"],bbox_to_anchor=(1.2,0.9))

        ax.axis('equal')
        plt.tight_layout()
        buf = io.BytesIO()  # Grafik için bir bayt akışı oluşturun
        plt.savefig(buf, format='png')  # Grafik dosyasını bayt akışına PNG formatında kaydedin
        buf.seek(0)  # Bayt akışını başa sıfırlayın
        string = base64.b64encode(buf.read())  # Bayt akışını base64 kodlayın
        uri = urllib.parse.quote(string)  # Base64 kodunu URL uyumlu hale getirin
        return uri