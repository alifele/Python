import numpy as np
import matplotlib.pyplot as plt
import cv2
import pdb
import copy


# ██████   █████  ██████   █████  ███    ███ ███████ ████████ ███████ ██████  ███████
# ██   ██ ██   ██ ██   ██ ██   ██ ████  ████ ██         ██    ██      ██   ██ ██
# ██████  ███████ ██████  ███████ ██ ████ ██ █████      ██    █████   ██████  ███████
# ██      ██   ██ ██   ██ ██   ██ ██  ██  ██ ██         ██    ██      ██   ██      ██
# ██      ██   ██ ██   ██ ██   ██ ██      ██ ███████    ██    ███████ ██   ██ ███████



VL_triangles = 8
L_triangles = 8
L_block_width = 20
M_triangles = 42
M_block_width = 40
S_triangles = 512
S_box_half_size = 40

population_size = 200
number_of_iterations = 300


cross_over_ratio = 0.75
mutation_ratio = 0.12
golden_transfer_ratio = 0.13



image = cv2.imread('monalisa_image.jpg')
clear_dim = (int(image.shape[1]//100 * 100), int(image.shape[0]//100 * 100))
image = cv2.resize(image, clear_dim)

##
blocks_row = [(10*i,(i+1)*10) for i in range(int(image.shape[0]/10))]
blocks_col = [(10*i,(i+1)*10) for i in range(int(image.shape[1]/10))]

##



# ██ ███    ██ ██████  ██ ██    ██ ██ ██████  ██    ██  █████  ██      ███████
# ██ ████   ██ ██   ██ ██ ██    ██ ██ ██   ██ ██    ██ ██   ██ ██      ██
# ██ ██ ██  ██ ██   ██ ██ ██    ██ ██ ██   ██ ██    ██ ███████ ██      ███████
# ██ ██  ██ ██ ██   ██ ██  ██  ██  ██ ██   ██ ██    ██ ██   ██ ██           ██
# ██ ██   ████ ██████  ██   ████   ██ ██████   ██████  ██   ██ ███████ ███████




class My_draw:
    def __init__(self):
        self.VL_gene = []
        self.L_gene = []
        self.M_gene = []
        self.S_gene = []
        self.fitness = 0



    def init_genes(self):
        self.init_VL_genes()
        self.init_L_genes()
        self.init_M_genes()
        self.init_S_genes()


    def set_genes(self, new_VL_gene, new_L_gene, new_M_gene, new_S_gene):
        self.VL_gene = copy.deepcopy(new_VL_gene)
        self.L_gene = copy.deepcopy(new_L_gene)
        self.M_gene = copy.deepcopy(new_M_gene)
        self.S_gene = copy.deepcopy(new_S_gene)

    def init_S_genes(self):
        for i in range(S_triangles):
            p_list = []
            rand_y = np.random.randint(image.shape[0])
            rand_x = np.random.randint(image.shape[1])
            for i in range(3):
                delta_rand = np.random.randint(-S_box_half_size, S_box_half_size, size = 2)
                p_list.append([rand_x + delta_rand[0], rand_y + delta_rand[1] ])

            p_list = np.array(p_list)
            color_rand = np.random.randint(255, size=3, dtype='int')
            color = [int(color_rand[0]), int(color_rand[1]), int(color_rand[2])]
            self.S_gene.append([p_list, color])

    def init_L_genes(self):
        for i in range(L_triangles):
            pos_list = [[[0,L_block_width],[0,L_block_width]]
                        ,[[0,L_block_width],[-L_block_width,-1]]
                        ,[[-L_block_width,-1],[-L_block_width,-1]]
                        ,[[-L_block_width,-1],[0,L_block_width]]]

            np.random.shuffle(pos_list)
            p_list = []
            for i in range(3):
                row_block = (blocks_row[pos_list[i][0][0]][0],blocks_row[pos_list[i][0][1]][-1])
                col_block = (blocks_col[pos_list[i][1][0]][0],blocks_col[pos_list[i][1][1]][-1])
                pos_y = np.random.randint(*row_block)
                pos_x = np.random.randint(*col_block)
                p_list.append([pos_x, pos_y])

            p_list = np.array(p_list)
            color_rand = np.random.randint(255, size=3, dtype='int')
            color = [int(color_rand[0]), int(color_rand[1]), int(color_rand[2])]
            self.L_gene.append([p_list, color])

    def init_M_genes(self):
        for i in range(M_triangles):
            pos_list = [[[0,M_block_width],[0,M_block_width]]
                        ,[[0,M_block_width],[-M_block_width,-1]]
                        ,[[-M_block_width,-1],[-M_block_width,-1]]
                        ,[[-M_block_width,-1],[0,M_block_width]]]

            np.random.shuffle(pos_list)
            p_list = []
            for i in range(3):
                row_block = (blocks_row[pos_list[i][0][0]][0],blocks_row[pos_list[i][0][1]][-1])
                col_block = (blocks_col[pos_list[i][1][0]][0],blocks_col[pos_list[i][1][1]][-1])
                pos_y = np.random.randint(*row_block)
                pos_x = np.random.randint(*col_block)
                p_list.append([pos_x, pos_y])

            p_list = np.array(p_list)
            color_rand = np.random.randint(255, size=3, dtype='int')
            color = [int(color_rand[0]), int(color_rand[1]), int(color_rand[2])]
            self.M_gene.append([p_list, color])

    def init_VL_genes(self):
        for i in range(VL_triangles):
            pos_list = [[0,0],[0,-1],[-1,-1],[-1,0]] # first -> row, second -> col
            np.random.shuffle(pos_list)

            p_list = []
            for i in range(3):
                row_block = blocks_row[pos_list[i][0]]
                col_block = blocks_col[pos_list[i][1]]
                pos_y = np.random.randint(*row_block)
                pos_x = np.random.randint(*col_block)
                p_list.append([pos_x, pos_y])
            p_list = np.array(p_list)
            color_rand = np.random.randint(255, size=3, dtype='int')
            color = [int(color_rand[0]), int(color_rand[1]), int(color_rand[2])]
            self.VL_gene.append([p_list, color])
            #cv2.drawContours(self.mat, [p_list], 0, color, -1)
            #cv2.rectangle(self.mat, (10,10),(30,50),(100,0,0),-1)

    def draw(self):
        self.mat = np.zeros(image.shape, dtype='uint8')
        for elem in self.VL_gene:
            cv2.drawContours(self.mat, [elem[0]], 0, elem[1], -1)
        for elem in self.L_gene:
            cv2.drawContours(self.mat, [elem[0]], 0, elem[1], -1)
        for elem in self.M_gene:
            cv2.drawContours(self.mat, [elem[0]], 0, elem[1], -1)
        for elem in self.S_gene:
            cv2.drawContours(self.mat, [elem[0]], 0, elem[1], -1)

    def calc_fitness(self):
        self.draw()
        self.fitness = np.sum(self.mat == image)
        del self.mat
        return self.fitness



#  ██████  ███████ ███    ██ ███████ ████████ ██  ██████
# ██       ██      ████   ██ ██         ██    ██ ██
# ██   ███ █████   ██ ██  ██ █████      ██    ██ ██
# ██    ██ ██      ██  ██ ██ ██         ██    ██ ██
#  ██████  ███████ ██   ████ ███████    ██    ██  ██████





class Genetic:
    def __init__(self):
        self.create_initial_pop()


    def draw_best_monaliza(self):
        elem = int(self.score_list[0][0])
        self.init_pop_list[elem].draw()
        rand = np.random.randint(1000)
        plt.plot(self.best_scores); plt.savefig('monalisa{}'.format(rand))
        cv2.imwrite('monalisa_image{}.png'.format(rand), self.init_pop_list[elem].mat)
        cv2.imshow('win', self.init_pop_list[elem].mat)
        cv2.waitKey()
        cv2.destroyAllWindows()




    def run(self):
        self.best_scores = []
        for i in range(number_of_iterations):
            self.next_generation()
            self.init_pop_list = copy.deepcopy(self.new_pop_list)
            self.score_list = copy.deepcopy(self.new_score_list)
            self.best_scores.append(self.score_list[0][1])
            print(i)





    def create_initial_pop(self):
        self.init_pop_list = []
        self.score_list = []
        for i in range(population_size):
            self.init_pop_list.append(My_draw())
            self.init_pop_list[-1].init_genes()
            fitness = self.init_pop_list[-1].calc_fitness()
            self.score_list.append([i, fitness, -1.0, -1.0])  # [index, fitness, normal_fitness, accum]


        self.score_list = np.array(self.score_list)
        self.score_list[:,2] = self.score_list[:,1] / self.score_list[:,1].sum()
        self.score_list = self.score_list[self.score_list[:,1].argsort()][::-1]


        self.score_list[0,3] = self.score_list[0,2]
        for i in range(1, len(self.score_list)):
            self.score_list[i,3] = self.score_list[i-1,3] + self.score_list[i,2]



    def next_generation(self):
        self.new_pop_list = []

        self.golden_transfer()
        self.cross_over()
        self.mutate()
        self.random_transfer()

        self.new_score_list = []
        for i in range(population_size):
            fitness = self.new_pop_list[i].calc_fitness()
            self.new_score_list.append([i, fitness, -1.0, -1.0])  # [index, fitness, normal_fitness, accum]

        self.new_score_list = np.array(self.new_score_list)
        self.new_score_list[:,2] = self.new_score_list[:,1] / self.new_score_list[:,1].sum()
        self.new_score_list = self.new_score_list[self.new_score_list[:,1].argsort()][::-1]

        self.new_score_list[0,3] = self.new_score_list[0,2]
        for i in range(1, len(self.new_score_list)):
            self.new_score_list[i,3] = self.new_score_list[i-1,3] + self.new_score_list[i,2]


    def golden_transfer(self):
        for i in range(int(golden_transfer_ratio*population_size)):
            elem = int(self.score_list[i][0])
            self.new_pop_list.append(My_draw())
            self.new_pop_list[-1].set_genes( self.init_pop_list[elem].VL_gene
                                          , self.init_pop_list[elem].L_gene
                                          , self.init_pop_list[elem].M_gene
                                          , self.init_pop_list[elem].S_gene)



    def cross_over(self):
        for i in range(int(cross_over_ratio*population_size//2)):

            rand = np.random.random(2)

            score_list_ind1 = np.argmax(rand[0] < self.score_list[:,3])
            score_list_ind2 = np.argmax(rand[1] < self.score_list[:,3])

            draw_ind1 = int(self.score_list[score_list_ind1][0])
            draw_ind2 = int(self.score_list[score_list_ind2][0])

            draw1 = self.init_pop_list[draw_ind1]
            draw2 = self.init_pop_list[draw_ind2]

            VL_gene_1 = copy.deepcopy(draw1.VL_gene)
            L_gene_1 = copy.deepcopy(draw1.L_gene)
            M_gene_1 = copy.deepcopy(draw1.M_gene)
            S_gene_1 = copy.deepcopy(draw1.S_gene)

            VL_gene_2 = copy.deepcopy(draw2.VL_gene)
            L_gene_2 = copy.deepcopy(draw2.L_gene)
            M_gene_2 = copy.deepcopy(draw2.M_gene)
            S_gene_2 = copy.deepcopy(draw2.S_gene)

            VL_cross_over_rand = np.random.randint(len(VL_gene_1))
            L_cross_over_rand = np.random.randint(len(L_gene_1))
            M_cross_over_rand = np.random.randint(len(M_gene_1))
            S_cross_over_rand = np.random.randint(len(S_gene_1))

            temp1 = copy.deepcopy(VL_gene_1[:VL_cross_over_rand])
            VL_gene_1[:VL_cross_over_rand] = copy.deepcopy(VL_gene_2[:VL_cross_over_rand])
            VL_gene_2[:VL_cross_over_rand] = copy.deepcopy(temp1)

            temp1 = copy.deepcopy(L_gene_1[:L_cross_over_rand])
            L_gene_1[:L_cross_over_rand] = copy.deepcopy(L_gene_2[:L_cross_over_rand])
            L_gene_2[:L_cross_over_rand] = copy.deepcopy(temp1)

            temp1 = copy.deepcopy(M_gene_1[:M_cross_over_rand])
            M_gene_1[:M_cross_over_rand] = copy.deepcopy(M_gene_2[:M_cross_over_rand])
            M_gene_2[:M_cross_over_rand] = copy.deepcopy(temp1)

            temp1 = copy.deepcopy(S_gene_1[:S_cross_over_rand])
            S_gene_1[:S_cross_over_rand] = copy.deepcopy(S_gene_2[:S_cross_over_rand])
            S_gene_2[:S_cross_over_rand] = copy.deepcopy(temp1)

            self.new_pop_list.append(My_draw())
            self.new_pop_list[-1].set_genes( VL_gene_1
                                          ,L_gene_1
                                          ,M_gene_1
                                          ,S_gene_1)

            self.new_pop_list.append(My_draw())
            self.new_pop_list[-1].set_genes( VL_gene_2
                                          ,L_gene_2
                                          ,M_gene_2
                                          ,S_gene_2)




    def mutate(self):
        for i in range(int(mutation_ratio*population_size)):
            self.new_pop_list.append(My_draw())
            self.new_pop_list[-1].init_genes()


    def random_transfer(self):
        n = population_size - len(self.new_pop_list)

        for i in range(n):
            rand = np.random.random(2)
            score_list_ind1 = np.argmax(rand[0] < self.score_list[:,3])
            draw_ind1 = int(self.score_list[score_list_ind1][0])
            draw1 = self.init_pop_list[draw_ind1]

            VL_gene_1 = copy.deepcopy(draw1.VL_gene)
            L_gene_1 = copy.deepcopy(draw1.L_gene)
            M_gene_1 = copy.deepcopy(draw1.M_gene)
            S_gene_1 = copy.deepcopy(draw1.S_gene)

            self.new_pop_list.append(My_draw())
            self.new_pop_list[-1].set_genes( VL_gene_1
                                          ,L_gene_1
                                          ,M_gene_1
                                          ,S_gene_1)








# ███    ███  █████  ██ ███    ██
# ████  ████ ██   ██ ██ ████   ██
# ██ ████ ██ ███████ ██ ██ ██  ██
# ██  ██  ██ ██   ██ ██ ██  ██ ██
# ██      ██ ██   ██ ██ ██   ████




genetic = Genetic()
genetic.run()
genetic.draw_best_monaliza()
#cv2.imshow('win', my_draw.mat)
#cv2.waitKey(0)
#cv2.destroyAllWindows()
##
