"""
定义一个用于根据传入的一批商品信息（商品名、价格、数量）、优惠（优惠券、积分抵扣）、运费信息计算订单的总金额的函数。
具体如下：
    1.优惠券需要商品满5000才可以使用，且优惠券金额不能超过商品总价。
    2.积分抵扣需要商品总金额满5000才可以使用，100积分抵扣1元（且抵扣金额不能超过商品总价，积分只能整百抵扣）
"""

def commerce_calculation (*args,coupon,points,shipping):
    """
    :param args: 商品信息
    :param coupon: 优惠券
    :param points: 积分
    :param shipping: 运费
    """
    # 1.商品总价
    total_print = [goods[1] * goods[2] for goods in args]
    total = sum(total_print)
    total_cost = total

    # 2.扣除优惠券
    if total >= 5000  and coupon <= total:
        total_cost -= coupon
        print(f"优惠券抵扣：{coupon}")

    # 3.扣除积分
    if total >= 5000 and points // 100 <= total:
        total_cost -= points // 100

    # 4.加上运费
    total_cost += shipping
    return print(f"订单总价为：{total_cost}")


commerce_calculation(('手机', 5000, 1), ('电脑', 5000, 1), ('鼠标', 500, 1), coupon=500, points=1000, shipping=10)