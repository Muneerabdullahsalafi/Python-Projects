# install the pynput module to run this Code
# Command = pip install pynput

import pynput
from pynput.keyboard import Key, Controller
import time

keyboard = Controller()

time.sleep(2)

for char in "Lorem ipsum dolor sit amet consectetur adipisicing elit. Eaque, nesciunt? Animi ab iste distinctio, nostrum minus ipsam vitae quisquam quam perspiciatis. Doloribus assumenda, itaque quam a omnis hic vel quis sunt, magni reiciendis blanditiis delectus ipsum animi exercitationem, architecto officiis sequi quaerat! Suscipit quasi id saepe incidunt facere quaerat! Pariatur placeat, eveniet ad sunt fugiat veniam reprehenderit porro! Saepe ipsum eius aperiam ad asperiores! Repellat ipsum, nemo error architecto est voluptate modi veniam hic, incidunt animi officiis. Odit, debitis sapiente? Beatae blanditiis impedit ipsam veritatis a, modi dolor voluptate delectus. Ex sequi cum dolor eos, neque ea incidunt cupiditate nobis qui obcaecati doloribus eum possimus perferendis, velit quia ullam vero. Quaerat, odit aliquid, laudantium delectus excepturi soluta impedit officia libero iste assumenda temporibus quidem architecto tempore, dolorum quis ut unde provident illum pariatur quas maiores dolores? Voluptatum, sit quae! Molestiae voluptas id, repellendus minus nihil sunt mollitia quos rerum tempore reprehenderit amet ipsum, labore neque natus perspiciatis a exercitationem rem ratione ullam. Placeat minima possimus dolore totam vero facilis! Nesciunt itaque earum ducimus deserunt eligendi inventore maxime praesentium unde repellendus repellat non ab impedit veritatis architecto voluptatem cum qui tenetur harum, numquam quod neque fugit. Porro numquam nostrum voluptatibus exercitationem maxime fugit modi, hic ipsum, aut veritatis ut neque, ullam perferendis tenetur ad? Commodi architecto aperiam cum provident maiores ut nemo sint reiciendis quis? Vero alias sunt aliquam iusto temporibus non a, quas eius neque ullam? Saepe consequuntur voluptas ex sapiente maxime hic impedit nisi corporis dignissimos soluta veritatis, sequi dolorem, veniam odit asperiores corrupti nemo ratione! Alias ex distinctio quia tenetur possimus vel pariatur perspiciatis voluptatibus error optio saepe ea, temporibus harum voluptas blanditiis. Quisquam in velit excepturi minima beatae laudantium tempora similique voluptate ad inventore tenetur, pariatur ea commodi dolor quaerat enim id incidunt veritatis. Ipsum explicabo doloremque suscipit aperiam, aliquid accusamus maxime, amet debitis natus iusto sit quae reprehenderit facere fuga vitae deleniti temporibus culpa! Officiis suscipit, possimus optio tempora doloremque quidem dolorem assumenda at totam numquam nesciunt laudantium. Corporis in deleniti voluptate cupiditate soluta alias earum dolorum ducimus optio aliquam, debitis aliquid harum odit blanditiis ullam ratione necessitatibus possimus fugiat doloremque sint nobis ipsum autem recusandae. Libero ab optio amet, blanditiis vero maxime nisi. Mollitia nihil quidem voluptatem ratione vero itaque maxime exercitationem quam et, est expedita! Harum temporibus, repudiandae asperiores enim omnis saepe quasi perferendis! Voluptatibus quae suscipit iste consequatur delectus, in fuga, at nesciunt pariatur, optio sunt ipsam veniam ex! Fugiat maiores accusamus voluptate, delectus debitis assumenda fuga, suscipit magnam, vel ad tempora praesentium ab iste quasi! Nobis sunt quisquam aut dignissimos porro perspiciatis laboriosam, cupiditate dolor eveniet blanditiis itaque, cumque nihil at aliquam, temporibus omnis autem modi. Iste illum quas consequatur officiis quidem laboriosam quam a atque dolores impedit magni tempora alias, dignissimos error excepturi veniam odio reprehenderit ducimus similique itaque debitis doloremque! Aut illo adipisci vitae dignissimos dolores rem delectus quibusdam fugit atque similique aperiam exercitationem nobis quod optio maiores explicabo, eveniet quisquam sint sit minima. Velit eligendi, deleniti deserunt praesentium earum nemo obcaecati iure ea blanditiis accusantium maiores porro nulla illo itaque mollitia rerum dolor? Fuga maxime et itaque nisi? Minus quasi eligendi repellat sit error blanditiis illo, odit ipsa eos neque et fuga necessitatibus repudiandae doloribus molestias delectus est! Vero laudantium quia cumque nostrum, quaerat dicta dolore reprehenderit numquam animi rem totam rerum officiis magnam! Officiis minus ipsam iste provident culpa necessitatibus deleniti, sit aperiam quae fugit nihil esse blanditiis nemo repellendus impedit. Possimus, expedita alias veritatis soluta suscipit doloribus officia libero exercitationem, voluptas quis omnis temporibus quidem sit ipsum sed nemo, in enim eligendi similique officiis quae aliquid praesentium? Ipsum nobis laborum perferendis magni provident. Ipsam sit nostrum accusantium, doloribus maxime aliquam unde id voluptatibus facilis. Aut quisquam fugit esse est eligendi laborum distinctio rerum illo dolorum accusantium amet vel, iure quos debitis eos reiciendis quae alias nisi dolore. Quod nesciunt dolores placeat, voluptatibus voluptatum, temporibus dolorum a harum eaque excepturi ullam provident eius nostrum hic numquam, ducimus delectus repellendus nam unde explicabo officiis aut vero nisi! Ut natus veniam iure ad consectetur voluptate tenetur voluptas nam aliquid quaerat asperiores sint quas sit facere nostrum repellendus, neque deserunt quia sequi beatae accusamus impedit. Ad, nemo aspernatur tenetur incidunt voluptates, mollitia nulla earum distinctio possimus quae asperiores eum necessitatibus deserunt a reiciendis similique veniam ipsum. Ad quae omnis tempore laboriosam veritatis praesentium adipisci quibusdam debitis vero voluptatem, error nam quaerat ut aspernatur magni ratione nostrum culpa totam? Possimus numquam enim libero pariatur optio delectus ipsam quis cum corporis et dolores veritatis nesciunt, debitis minima nemo tempore cupiditate culpa? Ea, sapiente. Veritatis, corporis consequuntur libero magnam nisi saepe est quibusdam. Nulla quas impedit eveniet enim veniam natus mollitia, laboriosam necessitatibus quisquam iusto repudiandae rerum quia temporibus cumque magnam porro distinctio. Doloribus obcaecati, quibusdam praesentium fugit libero corrupti totam maxime eum debitis asperiores vitae cupiditate nemo natus quo blanditiis in voluptate minus expedita nisi! At, itaque voluptas quo debitis in minus cumque expedita, tempore eius cum laudantium, exercitationem accusamus reprehenderit laborum voluptates laboriosam amet. Minus nam laudantium tempore distinctio voluptatibus repellat dolore asperiores laborum cupiditate sint iste doloribus placeat perspiciatis adipisci, aliquid aperiam totam nemo eum dicta qui nulla quam. Ratione omnis consequuntur dolorem illo similique aut aliquam mollitia, voluptates inventore veritatis deserunt adipisci, ipsam praesentium temporibus fugiat officia eum nam ut error modi sequi eligendi eaque exercitationem? Odio assumenda harum fugit autem ut ducimus maxime aut esse. Repudiandae quibusdam dolores impedit nihil iste, ea, harum earum necessitatibus libero sequi sed error cum aperiam natus reiciendis obcaecati dolorum, architecto blanditiis ex nam maiores ratione! Minima dolorem quisquam cupiditate ea commodi placeat quis perspiciatis? Obcaecati molestiae praesentium eos, enim error deleniti blanditiis ab, veniam alias nesciunt animi laudantium sapiente accusantium iure tenetur minus cumque tempora esse nemo ipsum voluptates, perferendis dicta quam quae? Necessitatibus omnis, enim accusantium voluptates accusamus qui error dolor et atque. Nobis fugit dicta eum, temporibus suscipit obcaecati incidunt odio tenetur impedit optio in error natus minima nihil quisquam amet sequi magnam eveniet similique et perferendis maxime? At exercitationem perspiciatis fuga quam, rem et illum itaque quasi nemo qui nam aut in porro laborum sint commodi dolore, accusantium natus expedita. Consectetur tempore esse veniam impedit quaerat dolores pariatur consequatur. Laudantium pariatur officiis rem illum exercitationem quis. Nostrum molestiae ad dignissimos harum ullam, dolor repellat quae officiis suscipit laborum iure nihil esse odit debitis, eius beatae optio, dicta eligendi est. Explicabo, consectetur, aut culpa reiciendis quibusdam exercitationem minima beatae quidem aliquam accusantium error numquam, dolorem pariatur est. Deserunt tenetur, recusandae numquam ab expedita qui quas rerum, veniam harum eaque natus ex. Voluptate quos reiciendis nihil animi recusandae ab doloribus ea odio vero aspernatur! Neque aut eveniet aliquam dolores molestiae similique nam, omnis facere nesciunt? Repudiandae sit dicta nam voluptatum accusamus, libero id necessitatibus. Quae, quasi nostrum facilis id iste animi. Laudantium suscipit similique repellat sed nam magni exercitationem, corrupti nisi neque dignissimos veniam, incidunt culpa voluptate aut fugiat nostrum natus officia expedita quam! Ullam molestias atque earum reiciendis libero id doloremque fugit. Veniam at deleniti numquam laudantium! Officia natus maxime eius, quibusdam tenetur nulla deleniti vero saepe maiores enim? Maxime officia itaque recusandae, doloremque placeat et? Corporis obcaecati, temporibus a possimus eius repellendus, enim facere, est facilis sequi quis vitae deserunt. Et ducimus officia distinctio quidem, delectus asperiores. Laboriosam saepe eaque reprehenderit expedita nesciunt qui, quae sit fuga nemo. Excepturi placeat iste enim odit aut assumenda, explicabo beatae similique, error numquam perspiciatis rem, doloremque corrupti porro quae autem? Recusandae sapiente ipsa nulla harum aperiam veniam libero quis quo animi maiores est odio labore laudantium commodi dolorum enim fuga, temporibus quos. Ullam rem, ratione officiis illum cumque vel eaque sequi delectus earum dolores eligendi repellat, officia alias fuga amet distinctio similique impedit. Id sint neque commodi laboriosam assumenda esse! Provident vel nostrum minus ratione consequatur ad numquam quasi porro cumque voluptate culpa optio mollitia suscipit vitae quis, quam earum. Voluptas nisi ex consequatur voluptate amet magni eum numquam provident doloribus quam sunt delectus est deleniti sint rerum, rem earum ipsa, odit, esse neque quaerat tempora velit. Est, vel aut assumenda modi voluptatibus porro quas reprehenderit neque eum inventore architecto provident, cupiditate molestiae blanditiis culpa odit tempora vitae ratione vero adipisci veritatis repellendus officiis? Enim corrupti adipisci soluta nobis sed impedit possimus laudantium vero, velit, officia quae ullam recusandae. Perspiciatis eos voluptatum rem quisquam neque consequuntur vitae repellendus, ipsum nobis unde delectus officiis recusandae ab maiores earum vero laborum, repellat assumenda eligendi cupiditate quod corporis dolor soluta? Culpa at nihil cum laboriosam, corporis odio officia id unde nostrum numquam sequi, vitae assumenda dolorum recusandae quae dolor qui laudantium sit aliquid omnis iste. Incidunt perspiciatis exercitationem inventore cumque corporis qui quisquam laudantium tempore doloribus aperiam, sit obcaecati reiciendis temporibus distinctio earum nisi omnis itaque. Ea, voluptatibus. Officiis impedit explicabo libero fugit non quaerat soluta recusandae distinctio id harum ab et officia, magni, consequatur cum? Quae reiciendis accusamus, nulla consequatur, earum pariatur aspernatur aliquid et sequi sapiente illum eum officia assumenda repellat ipsam quaerat natus reprehenderit praesentium. Nisi deleniti ratione nihil vero laudantium aspernatur consequuntur sapiente? Voluptatem accusantium, ex ratione odio nesciunt quam eveniet voluptas dolore quod omnis ipsam obcaecati ipsum iure minima at vero sapiente possimus harum tenetur earum reprehenderit voluptate, sequi quo perspiciatis? Aperiam voluptatibus aliquam sed vitae quasi voluptas incidunt in reprehenderit ad, placeat magnam animi saepe obcaecati qui minus ipsam. Tempore sapiente aliquam praesentium nobis asperiores beatae reprehenderit, porro dolore. Corrupti ullam accusantium cupiditate culpa modi consectetur quis libero laudantium porro dolorum. Atque laudantium optio quam soluta vitae dolorum, rerum itaque nobis veritatis alias magni vel animi incidunt autem quis esse repudiandae tenetur error. Pariatur beatae sunt non sint recusandae earum consequatur neque iure quis, nobis saepe, hic voluptatibus impedit consequuntur voluptatum. Accusamus delectus modi dicta blanditiis sit explicabo! Odit, corrupti id perspiciatis qui fugiat vitae assumenda vero, dignissimos, possimus sit temporibus ipsum expedita nobis natus quam? Esse, ducimus sed? Voluptatem suscipit dicta nulla laudantium sapiente tempore sint modi aspernatur, non qui maxime cum vitae, autem ipsum at. Perspiciatis illo temporibus repudiandae, saepe doloremque quo voluptates consequatur hic iusto dolorem. At iusto nobis dolores non sit debitis adipisci, distinctio recusandae nulla. Ipsam ut minima quo perspiciatis maiores, distinctio numquam sed, mollitia maxime nisi aspernatur unde placeat? Omnis eaque quasi cupiditate nemo quae suscipit, temporibus, neque laborum obcaecati voluptates exercitationem nostrum sunt aspernatur beatae sapiente. Hic laborum qui minima quidem deleniti. Soluta corporis repellendus architecto quis ipsa earum enim voluptas, nobis magnam possimus facere ex veniam? Corporis nemo beatae cupiditate. Maiores veniam non eligendi aperiam animi blanditiis quibusdam. Ducimus excepturi ratione fugiat, laboriosam sit similique iusto quo dignissimos magni neque at quae reprehenderit. A nemo velit totam unde, nulla ipsam odio facilis quisquam possimus sequi exercitationem incidunt necessitatibus voluptates, aspernatur soluta temporibus quibusdam itaque cupiditate quo sit accusantium ducimus. Dolores a dolorem, sapiente reprehenderit debitis qui veniam exercitationem officiis ipsum quo doloremque odio. Provident eum esse laborum accusantium possimus. Assumenda tempora ipsam soluta laborum. Sunt praesentium fugit maiores in! Quis hic perferendis ipsam libero odio! Dolorem voluptatem delectus quasi, rerum neque sunt ullam quo reprehenderit fuga odit in facere quae nobis aspernatur autem quisquam! Sed sint aspernatur, veniam praesentium voluptatem quasi eveniet nulla voluptate ipsam delectus consequatur eos. Minima in autem iusto architecto dicta officiis vel voluptate nemo repellat earum itaque, debitis, quidem ex dolore, dignissimos aliquid maiores labore ipsa amet nesciunt molestiae similique? Eius, vel dignissimos mollitia ad esse dolor dolorum incidunt consequatur quo eligendi odit nemo provident tenetur eum velit dolores ratione voluptate fuga! Quaerat, provident placeat! Vel quam, temporibus ipsam qui optio dolores, culpa eos commodi reprehenderit voluptatibus sint quaerat aperiam sequi dignissimos ratione quod dolor. Odit pariatur blanditiis voluptatibus saepe repudiandae excepturi suscipit. Doloribus omnis repellendus, quasi perferendis fugit dignissimos pariatur explicabo facilis. Ex porro ratione iste asperiores eveniet pariatur eum reprehenderit culpa placeat vero quisquam, delectus nisi sequi aut odio magnam assumenda voluptatibus fuga, aliquid inventore qui eaque? Tempora, quisquam? Asperiores veniam aperiam facere molestias sed, hic quos, iure, eligendi illum doloribus voluptatem deserunt excepturi quo ducimus iste nam soluta possimus saepe rem nobis iusto voluptas eos?dsgrrt asdkjfhlkjh jkjdhflkjhi Lorem ipsum dolor sit amet consectetur adipisicing elit. Eaque, nesciunt? Animi ab iste distinctio, nostrum minus ipsam vitae quisquam quam perspiciatis. Doloribus assumenda, itaque quam a omnis hic vel quis sunt, magni reiciendis blanditiis delectus ipsum animi exercitationem, architecto officiis sequi quaerat! Suscipit quasi id saepe incidunt facere quaerat! Pariatur placeat, eveniet ad sunt fugiat veniam reprehenderit porro! Saepe ipsum eius aperiam ad asperiores! Repellat ipsum, nemo error architecto est voluptate modi veniam hic, incidunt animi officiis. Odit, debitis sapiente? Beatae blanditiis impedit ipsam veritatis a, modi dolor voluptate delectus. Ex sequi cum dolor eos, neque ea incidunt cupiditate nobis qui obcaecati doloribus eum possimus perferendis, velit quia ullam vero. Quaerat, odit aliquid, laudantium delectus excepturi soluta impedit officia libero iste assumenda temporibus quidem architecto tempore, dolorum quis ut unde provident illum pariatur quas maiores dolores? Voluptatum, sit quae! Molestiae voluptas id, repellendus minus nihil sunt mollitia quos rerum tempore reprehenderit amet ipsum, labore neque natus perspiciatis a exercitationem rem ratione ullam. Placeat minima possimus dolore totam vero facilis! Nesciunt itaque earum ducimus deserunt eligendi inventore maxime praesentium unde repellendus repellat non ab impedit veritatis architecto voluptatem cum qui tenetur harum, numquam quod neque fugit. Porro numquam nostrum voluptatibus exercitationem maxime fugit modi, hic ipsum, aut veritatis ut neque, ullam perferendis tenetur ad? Commodi architecto aperiam cum provident maiores ut nemo sint reiciendis quis? Vero alias sunt aliquam iusto temporibus non a, quas eius neque ullam? Saepe consequuntur voluptas ex sapiente maxime hic impedit nisi corporis dignissimos soluta veritatis, sequi dolorem, veniam odit asperiores corrupti nemo ratione! Alias ex distinctio quia tenetur possimus vel pariatur perspiciatis voluptatibus error optio saepe ea, temporibus harum voluptas blanditiis. Quisquam in velit excepturi minima beatae laudantium tempora similique voluptate ad inventore tenetur, pariatur ea commodi dolor quaerat enim id incidunt veritatis. Ipsum explicabo doloremque suscipit aperiam, aliquid accusamus maxime, amet debitis natus iusto sit quae reprehenderit facere fuga vitae deleniti temporibus culpa! Officiis suscipit, possimus optio tempora doloremque quidem dolorem assumenda at totam numquam nesciunt laudantium. Corporis in deleniti voluptate cupiditate soluta alias earum dolorum ducimus optio aliquam, debitis aliquid harum odit blanditiis ullam ratione necessitatibus possimus fugiat doloremque sint nobis ipsum autem recusandae. Libero ab optio amet, blanditiis vero maxime nisi. Mollitia nihil quidem voluptatem ratione vero itaque maxime exercitationem quam et, est expedita! Harum temporibus, repudiandae asperiores enim omnis saepe quasi perferendis! Voluptatibus quae suscipit iste consequatur delectus, in fuga, at nesciunt pariatur, optio sunt ipsam veniam ex! Fugiat maiores accusamus voluptate, delectus debitis assumenda fuga, suscipit magnam, vel ad tempora praesentium ab iste quasi! Nobis sunt quisquam aut dignissimos porro perspiciatis laboriosam, cupiditate dolor eveniet blanditiis itaque, cumque nihil at aliquam, temporibus omnis autem modi. Iste illum quas consequatur officiis quidem laboriosam quam a atque dolores impedit magni tempora alias, dignissimos error excepturi veniam odio reprehenderit ducimus similique itaque debitis doloremque! Aut illo adipisci vitae dignissimos dolores rem delectus quibusdam fugit atque similique aperiam exercitationem nobis quod optio maiores explicabo, eveniet quisquam sint sit minima. Velit eligendi, deleniti deserunt praesentium earum nemo obcaecati iure ea blanditiis accusantium maiores porro nulla illo itaque mollitia rerum dolor? Fuga maxime et itaque nisi? Minus quasi eligendi repellat sit error blanditiis illo, odit ipsa eos neque et fuga necessitatibus repudiandae doloribus molestias delectus est! Vero laudantium quia cumque nostrum, quaerat dicta dolore reprehenderit numquam animi rem totam rerum officiis magnam! Officiis minus ipsam iste provident culpa necessitatibus deleniti, sit aperiam quae fugit nihil esse blanditiis nemo repellendus impedit. Possimus, expedita alias veritatis soluta suscipit doloribus officia libero exercitationem, voluptas quis omnis temporibus quidem sit ipsum sed nemo, in enim eligendi similique officiis quae aliquid praesentium? Ipsum nobis laborum perferendis magni provident. Ipsam sit nostrum accusantium, doloribus maxime aliquam unde id voluptatibus facilis. Aut quisquam fugit esse est eligendi laborum distinctio rerum illo dolorum accusantium amet vel, iure quos debitis eos reiciendis quae alias nisi dolor":
    keyboard.press(char)
    keyboard.release(char)
    time.sleep(1)
