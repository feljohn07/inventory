from django import forms
from products.models import Product

class ProductForm(forms.ModelForm):

    # product_image = forms.FileField(widget=forms.FileInput(attrs={'class': 'form-control mb-2'}))

    class Meta:

        model = Product

        fields = [
            # 'product_image',
            'product_name', 
            'supplier', 
            # 'product_category', 
            'price_per_piece',
            'retail_per_piece',
            'inventory_received',
            'minimum_required'
        ]

        widgets = {
            'product_name': forms.TextInput(attrs={'class': 'form-control mb-2'}),
            'supplier': forms.Select(attrs={'class': 'form-control mb-2'}),
            'product_category': forms.Select(attrs={'class': 'form-control mb-2'}),
            'price_per_piece': forms.NumberInput(attrs={'class': 'form-control mb-2'}),
            'retail_per_piece': forms.NumberInput(attrs={'class': 'form-control mb-2'}),
            'inventory_received': forms.NumberInput(attrs={'class': 'form-control mb-2'}),
            'minimum_required': forms.NumberInput(attrs={'class': 'form-control mb-2'}),
        }

        def clean(self):
            return self.cleaned_data

        


    # FRUIT_CHOICES= [
    # ('orange', 'Oranges'),
    # ('cantaloupe', 'Cantaloupes'),
    # ('mango', 'Mangoes'),
    # ('honeydew', 'Honeydews'),
    # ]
    
    # product_name = forms.CharField(label='Product Name', max_length=125)
    # supplier = forms.CharField(label='select', widget=forms.Select(choices=FRUIT_CHOICES))
    # product_category = forms.CharField(label='select', widget=forms.Select(choices= Category.objects.all().values_list()))

    # price_per_piece = forms.FloatField(label='Cost Price')
    # retail_per_piece = forms.FloatField(label='Selling Price')
    # inventory_received = forms.IntegerField(label='Received')
    # inventory_on_hand = forms.IntegerField(label='On Hand')
    


    # product_name        = models.CharField(max_length=125)
    # price_per_piece     = models.DecimalField(max_digits=10, decimal_places=2) # Cost Price
    # retail_per_piece    = models.DecimalField(max_digits=10, decimal_places=2) # Retail Price
    # inventory_received  = models.IntegerField(default=0, blank=True, null=True)
    # inventory_shipped   = models.IntegerField(default=0, blank=True, null=True)
    # inventory_on_hand   = models.IntegerField(default=0, blank=True, null=True)
    # minimum_required    = models.IntegerField(default=0, blank=True, null=True)

    # product_category    = models.ForeignKey('Category' , null=True ,on_delete = models.SET_NULL)
    # supplier            = models.ForeignKey(Supplier , null=True ,on_delete = models.SET_NULL)
    # created_at          = models.DateTimeField(default = datetime.now)
    # updated_at          = models.DateTimeField()
    