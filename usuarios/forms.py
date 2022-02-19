from django import forms


class Cadastro(forms.Form):
    sexos = [
        ('N', 'prefiro não informar'),
        ('M', 'masculino'),
        ('F', 'feminino')
    ]

    usuario = forms.CharField(
        label='',
        widget=forms.TextInput(attrs={'placeholder':'Como quer ser chamado'}))
    email = forms.EmailField(
        label='',
        widget=forms.EmailInput(attrs={'placeholder':'E-mail'})
    )
    senha = forms.CharField(
        label='',
        widget=forms.PasswordInput(attrs={'placeholder':'Senha'})
    )
    mes_aniversario = forms.DateField(label='')
    sexo = forms.ChoiceField(label='', choices=sexos)
    cpf = forms.CharField(
        label='',
        widget=forms.TextInput(attrs={'placeholder':'CPF'})
    )
    telefone = forms.CharField(
        label='',
        widget=forms.TextInput(attrs={'placeholder':'Telefone'})
    )
    cep = forms.CharField(
        label='',
        widget=forms.TextInput(attrs={'placeholder':'CEP'})
    )
    logradouro = forms.CharField(
        label='',
        widget=forms.TextInput(attrs={'placeholder':'logradouro'})
    )
    endereco_numero = forms.CharField(
        label='',
        widget=forms.TextInput(attrs={'placeholder':'Número'})
    )
    endereco_complemento = forms.CharField(
        label='',
        widget=forms.TextInput(attrs={'placeholder':'Complemento'})
    )
    endereco_referencia = forms.CharField(
        label='',
        widget=forms.TextInput(attrs={'placeholder':'Referencia'})
    )
    endereco_bairro = forms.CharField(
        label='',
        widget=forms.TextInput(attrs={'placeholder':'Bairro'})
    )
    estado = forms.CharField(label='')
    cidade = forms.CharField(label='')
    receber_novidades = forms.BooleanField(label='')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = ' formulario-input'

        self.fields['cpf'].widget.attrs['class'] += ' cpf'
        self.fields['cep'].widget.attrs['class'] += ' cep'
