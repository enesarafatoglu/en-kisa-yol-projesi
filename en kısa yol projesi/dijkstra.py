inf = float("inf")  # Sonsuz değeri tanımlar, bu değeri en uzak mesafeyi göstermek için kullanacağız.
start = "Çatı"  # Başlangıç noktası, algoritmanın başlayacağı yer.
stop = "Muradiye Toplanma Alanı"  # Hedef nokta, algoritmanın ulaşmak istediği yer.

graph = {}  # Graf yapısını oluşturmak için boş bir sözlük (dictionary) oluşturuluyor.

# Her bir nokta (düğüm) için diğer düğümlere olan mesafeler sözlükte saklanır.
graph["Çatı"] = {}
graph["Çatı"]["Develi"] = 107
graph["Çatı"]["Uslular"] = 29
graph["Çatı"]["Okul"] = 90

graph["Uzunyol"] = {}
graph["Uzunyol"]["Develi"] = 12

graph["Uslular"] = {}
graph["Uslular"]["Uzunyol"] = 159
graph["Uslular"]["Badırgalı"] = 104
graph["Uslular"]["Kaplıca"] = 214

graph["Develi"] = {}
graph["Develi"]["Kaplıca"] = 37

graph["Badırgalı"] = {}
graph["Badırgalı"]["Develi"] = 37

graph["Soğuk Çeşme"] = {}
graph["Soğuk Çeşme"]["Kaplıca"] = 135

graph["Okul"] = {}
graph["Okul"]["Soğuk Çeşme"] = 100
graph["Okul"]["Kaplıca"] = 137

graph["Kaplıca"] = {}
graph["Kaplıca"]["Muradiye Toplanma Alanı"] = 33

graph["Muradiye Toplanma Alanı"] = {}  # Hedef nokta olduğu için bağlantı içermiyor.

# Tüm düğümler için başlangıçta maliyet (cost) olarak sonsuz değeri atanıyor.
costs = {}
parents = {}

for node in graph:
    costs[node] = inf  # Her düğümün maliyeti başlangıçta sonsuz olarak ayarlanır.
    parents[node] = {}  # Her düğümün ebeveyni boş olarak başlatılır.

costs[start] = 0  # Başlangıç düğümünün maliyeti 0 olarak atanır çünkü kendisinden başlamaktadır.

# En düşük maliyetli düğümü bulmak için bir fonksiyon tanımlanır.
def find_cheapest_node(costs, not_checked):
    cheapest_node = None
    lowest_cost = inf
    for node in not_checked:
        if costs[node] <= lowest_cost:
            lowest_cost = costs[node]
            cheapest_node = node
    return cheapest_node

if __name__ == "__main__":
    not_checked = [node for node in costs]  # Henüz kontrol edilmemiş düğümleri tutan bir liste.
    node = find_cheapest_node(costs, not_checked)  # En düşük maliyetli düğüm bulunur.
    while not_checked:  # Henüz kontrol edilmemiş düğümler kaldığı sürece devam eder.
        cost = costs[node]  # Şu anki düğümün maliyeti alınır.
        child_cost = graph[node]  # Şu anki düğümün çocuklarına olan maliyetleri alınır.
        for c in child_cost:  # Her çocuk düğüm için:
            if costs[c] > cost + child_cost[c]:  # Yeni maliyet eski maliyetten düşükse:
                costs[c] = cost + child_cost[c]  # Maliyet güncellenir.
                parents[c] = node  # Ebeveyn düğüm güncellenir.
        not_checked.pop(not_checked.index(node))  # Kontrol edilen düğüm listeden çıkarılır.
        node = find_cheapest_node(costs, not_checked)  # Yeni en düşük maliyetli düğüm bulunur.
        m = costs[stop]  # Hedef düğümün maliyeti kaydedilir.
    
    # Tüm düğümler kontrol edildikten sonra sonuçlar yazdırılır.
    print(f"Mesafeler: {costs}")
    print(f"{start} -> {stop} arasındaki en kısa mesafe {m} metre")

    if costs[stop] < inf:  # Eğer hedef düğüme bir yol bulunmuşsa:
        path = [stop]  # Hedef düğümden başlayarak yol oluşturulur.
        i = 0
        while start not in path:  # Başlangıç düğümüne ulaşana kadar ebeveynler takip edilir.
            path.append(parents[path[i]])
            i += 1
        print(f"En kısa yol: {path[::-1]}")  # Yol ters çevrilip yazdırılır.
    else:
        print("Bir yol bulunmadı")  # Eğer hedef düğüme bir yol bulunamazsa, mesaj yazdırılır.

