def q1(p,q):
    price=p
    quantity=q
    gst=0.18
    delivery=60
    freedel=1500
    total=price*quantity
    gst_amt=total*gst
    if total>=1500:
        delivery=0
    else:
        pass
    final_amt=total+gst_amt+delivery
    print(f"Total : {total} GST : {gst_amt} Delivery: {delivery} Final Payable Amount: {final_amt}")
q1(800,2)
