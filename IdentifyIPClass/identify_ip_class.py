import requests
from bs4 import BeautifulSoup

# Verifica cabeçalhos de segurança comuns
def check_headers(url):
    try:
        response = requests.get(url)
        headers = response.headers

        # Verificar segurança de cabeçalhos comuns
        if 'X-Frame-Options' not in headers:
            print("Vulnerabilidade: X-Frame-Options não está configurado.")
        if 'X-Content-Type-Options' not in headers:
            print("Vulnerabilidade: X-Content-Type-Options não está configurado.")
        if 'Content-Security-Policy' not in headers:
            print("Vulnerabilidade: Content-Security-Policy não está configurado.")
    except requests.exceptions.RequestException as e:
        print(f"Erro ao acessar {url}: {e}")

# Verifica formulários para proteção CSRF
def check_forms(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        forms = soup.find_all('form')

        for form in forms:
            if 'csrf' not in form.prettify():
                print(f"Vulnerabilidade: Formulário em {url} sem proteção CSRF.")
    except requests.exceptions.RequestException as e:
        print(f"Erro ao acessar {url}: {e}")

# Verifica XSS em formulários e parâmetros de URL
def check_xss(url):
    xss_payload = "<script>alert('XSS')</script>"
    
    try:
        # Testar XSS em parâmetros de URL
        test_url = url + "?" + "test=" + xss_payload
        response = requests.get(test_url)
        if xss_payload in response.text:
            print(f"Vulnerabilidade XSS encontrada em URL: {test_url}")

        # Testar XSS em formulários
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        forms = soup.find_all('form')

        for form in forms:
            action = form.get('action')
            method = form.get('method')
            inputs = form.find_all('input')
            
            form_data = {}
            for input_tag in inputs:
                if input_tag.get('name'):
                    form_data[input_tag.get('name')] = xss_payload

            if action:
                form_action_url = url + action
            else:
                form_action_url = url

            if method and method.lower() == 'post':
                response = requests.post(form_action_url, data=form_data)
            else:
                response = requests.get(form_action_url, params=form_data)

            if xss_payload in response.text:
                print(f"Vulnerabilidade XSS encontrada em formulário: {form_action_url}")

    except requests.exceptions.RequestException as e:
        print(f"Erro ao acessar {url}: {e}")

def main():
    url = input("Digite a URL do site para verificar: ")
    print(f"Verificando vulnerabilidades em {url}...\n")

    check_headers(url)
    check_forms(url)
    check_xss(url)

if __name__ == "__main__":
    main()
